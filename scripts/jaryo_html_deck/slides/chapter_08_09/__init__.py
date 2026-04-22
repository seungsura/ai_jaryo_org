from __future__ import annotations

from . import slide_001
from . import slide_002
from . import slide_003
from . import slide_004
from . import slide_005
from . import slide_006
from . import slide_007
from . import slide_008
from . import slide_009
from . import slide_010
from . import slide_011
from . import slide_012
from . import slide_013

SLIDE_BUILDERS = [
    slide_001.build,
    slide_002.build,
    slide_003.build,
    slide_004.build,
    slide_005.build,
    slide_006.build,
    slide_007.build,
    slide_008.build,
    slide_009.build,
    slide_010.build,
    slide_011.build,
    slide_012.build,
    slide_013.build,
]

__all__ = ["SLIDE_BUILDERS"]
