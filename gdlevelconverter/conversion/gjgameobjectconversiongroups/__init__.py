"""
Defines a list of all groups in GJGameObject object id conversion
"""

from .grouplines import GroupLines
from .groupgroundspikes import GroupGroundSpikes
from .grouppillars import GroupPillars
from .groupslabs import GroupSlabs
from .groupcolor import GroupColor
from .groupglow import GroupGlow
from .groupclubstep import GroupClubstep
from .groupgears import GroupGears
from .groupgroundhazards import GroupGroundHazards
from .groupdecoration import GroupDecoration
from .grouptriggers import GroupTriggers
from .groupslopes import GroupSlopes
from .groupcircle import GroupCircle

GJGameObjectConversionGroups = [
    GroupSlopes,
    GroupTriggers,
    GroupDecoration,
    GroupGroundHazards,
    GroupGears,
    GroupClubstep,
    GroupGlow,
    GroupColor,
    GroupSlabs,
    GroupPillars,
    GroupGroundSpikes,
    GroupLines,
    GroupCircle
]

GJGameObjectConversionGroupsByName = {
    x.name: x for x in GJGameObjectConversionGroups}

GJGameObjectConversionSubGroups = {
    "base": [
        GroupSlopes,
        GroupTriggers,
        GroupDecoration,
        GroupGroundHazards,
        GroupGears,
        GroupGlow,
        GroupSlabs,
        GroupPillars,
        GroupLines
    ],
    "all": GJGameObjectConversionGroups
}
