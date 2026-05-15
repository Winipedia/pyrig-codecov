"""Test module."""

from pyrig.rig.tools.coverage_tester import CoverageTester


class TestCoverageTester:
    """Test class."""

    def test_version_control_ignore_paths(self) -> None:
        """Test method."""
        assert "coverage.xml" in CoverageTester.I.version_control_ignore_paths()

    def test_badge_urls(self) -> None:
        """Test method."""
        badge, url = CoverageTester.I.badge_urls()
        assert badge.startswith("https://codecov.io/gh/")
        assert badge.endswith("/graph/badge.svg")
        assert url.startswith("https://codecov.io/gh/")

    def test_remote_coverage_url(self) -> None:
        """Test method."""
        url = CoverageTester.I.remote_coverage_url()
        assert url.startswith("https://codecov.io/gh/")

    def test_access_token_key(self) -> None:
        """Test method."""
        assert CoverageTester.I.access_token_key() == "CODECOV_TOKEN"

    def test_additional_args(self) -> None:
        """Test method."""
        args = CoverageTester.I.additional_args()
        assert "--cov-report=xml" in args

    def test_threshold(self) -> None:
        """Test method."""
        assert CoverageTester.I.threshold() == 100  # noqa: PLR2004
