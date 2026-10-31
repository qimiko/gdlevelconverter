"""
Defines a list of all groups in GJGameObject object id conversion
"""

from .groupcircle import GroupCircle
from .groupclubstep import GroupClubstep
from .groupcolor import GroupColor
from .groupdecoration import GroupDecoration
from .groupgears import GroupGears
from .groupglow import GroupGlow
from .groupgroundhazards import GroupGroundHazards
from .groupgroundspikes import GroupGroundSpikes
from .grouplines import GroupLines
from .grouppillars import GroupPillars
from .grouppulsing import GroupPulsing
from .groupslabs import GroupSlabs
from .groupslopes import GroupSlopes
from .grouptriggers import GroupTriggers

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
    GroupCircle,
    GroupPulsing,
]

GJGameObjectConversionGroupsByName = {x.name: x for x in GJGameObjectConversionGroups}

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
        GroupLines,
    ],
    "all": GJGameObjectConversionGroups,
}
