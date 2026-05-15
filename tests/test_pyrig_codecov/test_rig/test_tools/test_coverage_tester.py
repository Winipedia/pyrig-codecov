"""Test module."""

from pyrig_codecov.rig.tools.coverage_tester import CoverageTester


class TestCoverageTester:
    """Test class."""

    def test_badge_urls(self) -> None:
        """Test method."""
        raise NotImplementedError

    def test_remote_coverage_url(self) -> None:
        """Test method."""
        raise NotImplementedError

    def test_access_token_key(self) -> None:
        """Test method."""
        raise NotImplementedError

    def test_additional_args(self) -> None:
        """Test method."""
        raise NotImplementedError

    def test_threshold(self) -> None:
        """Test method."""
        assert CoverageTester().threshold() == 100  # noqa: PLR2004
        assert CoverageTester.I.threshold() == 100  # noqa: PLR2004
