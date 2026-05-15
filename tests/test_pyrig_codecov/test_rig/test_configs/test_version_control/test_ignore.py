"""Test module."""

from pyrig_codecov.rig.configs.version_control.ignore import (
    VersionControllerIgnoreConfigFile,
)


class TestVersionControllerIgnoreConfigFile:
    """Test class."""

    def test_additional_ignore_lines(self) -> None:
        """Test method."""
        assert (
            "coverage.xml"
            in VersionControllerIgnoreConfigFile().additional_ignore_lines()
        )
