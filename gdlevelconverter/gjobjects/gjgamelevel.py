"""
GJGameLevel class definition
"""

import base64
import re

from .gjclient import GJClient
from .gjlevelstring import GJLevelString
from . import gjdictionary


class GJGameLevel(gjdictionary.GJDictionary):
    """
    Deserialized representation of a Geometry Dash level
    """

    # pylint: disable=too-many-instance-attributes
    # Geometry Dash levels are known to break convention.

    _definitions = [
        gjdictionary.ObjectDefinition(key="level_id", index="1"),
        gjdictionary.ObjectDefinition(key="name", index="2"),
        gjdictionary.ObjectDefinition(key="description", index="3"),
        gjdictionary.ObjectDefinition(
            key="level_string", index="4", deserialize_as=GJLevelString.from_encoded
        ),
        gjdictionary.ObjectDefinition(key="version", index="5", deserialize_as=int),
        gjdictionary.ObjectDefinition(
            key="audio_track", index="12", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(key="length", index="15", deserialize_as=int),
        gjdictionary.ObjectDefinition(key="auto", index="25", deserialize_as=int),
        gjdictionary.ObjectDefinition(key="two_player", index="31", deserialize_as=int),
        gjdictionary.ObjectDefinition(
            key="custom_song_track", index="35", deserialize_as=int
        ),
        gjdictionary.ObjectDefinition(key="capacity_string", index="36"),
    ]

    _splitter = ":"

    level_id: int
    name: str
    description: str
    "base64 encoded description of the level"
    level_string: GJLevelString
    version: int
    audio_track: int
    length: int
    auto: int
    two_player: int
    custom_song_track: int
    capacity_string: str

    binary_version: int

    @classmethod
    def from_gmd(cls, file: str):
        """
        Creates instance from gmd file contents
        """

        instance = cls()

        element_dict = gjdictionary.GJDictionary.from_dict_str(file)

        if "kCEK" not in element_dict or int(element_dict["kCEK"]) != 4:
            raise ValueError("gmd file is not representing a gameobject")

        # in the future i might make this as part of the gjdictionary class
        # i didn't feel it was necessary as this is only used once
        instance.level_id = int(element_dict.get("k1", 0))
        instance.name = element_dict.get("k2", "Unknown")

        description = element_dict.get("k3", "")
        is_old_gmd = element_dict.get("_data_version", 1) <= 1
        if description and is_old_gmd:
            # gmd files are double decoded, for some reason
            (null_removed,) = description.split("\x00")
            instance.description = base64.urlsafe_b64decode(null_removed).decode()
        else:
            instance.description = description.split("\x00")[0]

        # if this doesn't exist this should error
        instance.level_string = GJLevelString.from_encoded(element_dict["k4"])

        instance.audio_track = int(element_dict.get("k8", 1))
        instance.version = int(element_dict.get("k16", 1))
        instance.length = int(element_dict.get("k23", 0))
        instance.auto = int(element_dict.get("k33", 0))
        instance.two_player = int(element_dict.get("k43", 0))
        instance.custom_song_track = int(element_dict.get("k45", 0))
        instance.binary_version = int(element_dict.get("k50", 35))
        instance.capacity_string = element_dict.get("k67", "")

        return instance

    def to_gmd(self):
        """
        Creates gmd file from instance
        Based on GDShare source at the following link:
        https://github.com/HJfod/GDShare-mod/blob/38f00df3d1af115fb2ddca30b02d6acd12f89661/src/utils/gdshare.cpp#L150
        """

        description = base64.urlsafe_b64encode(self.description.encode()).decode()
        level_string = self.level_string.to_encoded()

        song_string = f"<k>k8</k><i>{self.audio_track}</i>"
        if self.custom_song_track > 0:
            song_string = f"<k>k45</k><i>{self.custom_song_track}</i>"

        return f"""<d>\
<k>kCEK</k><i>4</i>\
<k>k2</k><s>{self.name}</s>\
<k>k3</k><s>{description}</s>\
<k>k4</k><s>{level_string}</s>\
{song_string}\
<k>k13</k><t/>\
<k>k21</k><i>2</i>\
<k>k50</k><i>{self.binary_version}</i>\
</d>"""

    @classmethod
    def from_id(cls, client: GJClient, level_id: int):
        """
        Downloads an instance of level from id
        """
        resp = client.make_req(client.download_url, {"levelID": level_id})

        if resp.startswith("-"):
            raise ValueError(f"Download failed with code {resp}")

        return cls(resp)

    def upload(self, client: GJClient):
        """
        Uploads an instance of level
        """

        description = self.description
        if client.game_version < 20:
            # now we bother with unpacking description
            description = base64.urlsafe_b64decode(self.description).decode()
            description = re.sub(r"[^A-Za-z0-9\., \$\-\_\.\+\!\*()]", "", description)

        data = {
            "binaryVersion": self.binary_version,
            "udid": client.udid,
            "userName": client.user_name,
            "unlisted": 1,  # all levels are intentionally unlisted :)
            "levelDesc": description,
            "levelName": self.name,
            "levelVersion": self.version,
            "levelLength": self.length,
            "audioTrack": self.audio_track,
            "password": 1,  # hardcode all levels as free copy bc why not
            "levelID": 0,  # this technically has no purpose
            "original": self.level_id,
            "songID": self.custom_song_track,
            "objects": len(self.level_string.objects),
            "extraString": self.capacity_string,
            "auto": self.auto,
            "twoPlayer": self.two_player,
            "levelString": self.level_string.to_encoded(),
            # seed, seed2, wt, wt2, gdw, levelInfo would be required here for 2.1 upload
            # ldm, coins, requestedStars are not useful for 1.9 as well
        }

        resp = client.make_req(client.upload_url, data=data)

        if resp.startswith("-"):
            raise ValueError(f"Upload failed with code {resp}")

        return int(resp)
