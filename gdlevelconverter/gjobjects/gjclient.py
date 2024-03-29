"""
Defines GJClient class
"""

from dataclasses import dataclass
import urllib.request
import urllib.parse
from typing import Dict, Optional


@dataclass
class GJClient:
    """
    GJClient class for requests to Geometry Dash servers
    Not adding account support yet, I hope you feel pranked
    """

    game_version: int
    binary_version: Optional[int] = None
    download_url: str = "https://www.boomlings.com/database/downloadGJLevel22.php"
    upload_url: str = "https://www.boomlings.com/database/uploadGJLevel21.php"
    secret: str = "Wmfd2893gb7"
    udid: str = "S-hi-people"
    user_name: str = "21Reupload"

    def make_req(self, url: str, data: Dict[str, str]):
        """
        Makes a post request a url with data
        """

        data["secret"] = self.secret
        data["gameVersion"] = self.game_version

        if self.binary_version:
            data["binaryVersion"] = self.binary_version

        data_string = urllib.parse.urlencode(data).encode()

        req = urllib.request.Request(url, data=data_string)

        # remove user agent field
        opener = urllib.request.build_opener()
        opener.addheaders = [
            (header, value)
            for header, value in opener.addheaders
            if header.casefold() != "user-agent"
        ]

        with opener.open(req) as res:
            ret = res.read()

        return ret.decode()
