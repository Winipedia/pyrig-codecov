"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.tools.base.tool import Tool
from pyrig.rig.tools.testing.project import ProjectTester as BaseProjectTester

from pyrig_codecov.rig.tools.testing.project import ProjectTester

_TOOLS = (ProjectTester,)
_TOOLS_OVERRIDES = (
    BaseProjectTester.threshold,
    Tool.image_url,
)
