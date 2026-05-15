"""Coverage testing wrapper for the code coverage tool.

Wraps CoverageTester commands and information.
"""

from pyrig.rig.tools.coverage_tester import CoverageTester as BaseCoverageTester


class CoverageTester(BaseCoverageTester):
    """Overrides the base CoverageTester from pyrig."""

    def threshold(self) -> int:
        """Enforcing 100% coverage for packages with this plugin."""
        return 100
