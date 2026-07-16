"""Test module."""

from pathlib import Path

from pyrig.rig.configs.version_control.ignore import VersionControllerIgnoreConfigFile
from pyrig.rig.tools.base.tool import Tool

from pyrig_codecov.rig.tools.testing.project import ProjectTester


class TestProjectTester:
    """Test class."""

    def test_report_format(self) -> None:
        """Test method."""
        assert ProjectTester.I.report_format() == "xml"

    def test_image_url(self) -> None:
        """Test method."""
        assert ProjectTester.I.image_url().startswith("https://codecov.io/gh/")
        assert ProjectTester.I.image_url().endswith("/graph/badge.svg")

    def test_link_url(self) -> None:
        """Test method."""
        assert ProjectTester.I.link_url().startswith("https://codecov.io/gh/")

    def test_report_file(self) -> None:
        """Test method."""
        assert ProjectTester.I.report_file() == Path("coverage.xml")

    def test_version_control_ignore_patterns(self) -> None:
        """Test method."""
        assert "coverage.xml" in ProjectTester.I.version_control_ignore_patterns()
        assert (
            "coverage.xml"
            in VersionControllerIgnoreConfigFile.I.additional_ignore_lines()
        )

        patterns = ProjectTester.I.version_control_ignore_patterns()
        all_patterns = Tool.subclasses_version_control_ignore_patterns()
        assert all(pattern in all_patterns for pattern in patterns)

    def test_access_token_key(self) -> None:
        """Test method."""
        assert ProjectTester.I.access_token_key() == "CODECOV_TOKEN"

    def test_additional_args(self) -> None:
        """Test method."""
        args = ProjectTester.I.additional_args()
        assert "--cov-report=xml" in args

    def test_threshold(self) -> None:
        """Test method."""
        assert ProjectTester.I.threshold() == 100  # noqa: PLR2004
