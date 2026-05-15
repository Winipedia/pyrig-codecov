"""Test module."""

from pyrig_codecov.rig.tools.coverage_tester import CoverageTester


class TestCoverageTester:
    """Test class."""

    def test_threshold(self) -> None:
        """Test method."""
        assert CoverageTester().threshold() == 100  # noqa: PLR2004
        assert CoverageTester.I.threshold() == 100  # noqa: PLR2004
