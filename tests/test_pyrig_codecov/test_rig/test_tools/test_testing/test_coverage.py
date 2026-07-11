"""Test module."""

from pathlib import Path

from pyrig.rig.configs.version_control.ignore import VersionControllerIgnoreConfigFile

from pyrig_codecov.rig.tools.testing.coverage import CoverageTester


class TestCoverageTester:
    """Test class."""

    def test_report_format(self) -> None:
        """Test method."""
        assert CoverageTester.I.report_format() == "xml"

    def test_image_url(self) -> None:
        """Test method."""
        assert CoverageTester.I.image_url().startswith("https://codecov.io/gh/")
        assert CoverageTester.I.image_url().endswith("/graph/badge.svg")

    def test_link_url(self) -> None:
        """Test method."""
        assert CoverageTester.I.link_url().startswith("https://codecov.io/gh/")

    def test_report_file(self) -> None:
        """Test method."""
        assert CoverageTester.I.report_file() == Path("coverage.xml")

    def test_version_control_ignore_paths(self) -> None:
        """Test method."""
        assert "coverage.xml" in CoverageTester.I.version_control_ignore_paths()
        assert (
            "coverage.xml"
            in VersionControllerIgnoreConfigFile.I.additional_ignore_lines()
        )

    def test_remote_coverage_url(self) -> None:
        """Test method."""
        url = CoverageTester.I.remote_coverage_url()
        assert url.startswith("https://codecov.io/gh/")

    def test_access_token_key(self) -> None:
        """Test method."""
        assert CoverageTester.I.access_token_key() == "CODECOV_TOKEN"

    def test_additional_test_args(self) -> None:
        """Test method."""
        args = CoverageTester.I.additional_test_args()
        assert "--cov-report=xml" in args

    def test_threshold(self) -> None:
        """Test method."""
        assert CoverageTester.I.threshold() == 100  # noqa: PLR2004
