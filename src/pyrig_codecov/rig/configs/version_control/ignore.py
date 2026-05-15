"""Configuration management for .gitignore files."""

from pyrig.rig.configs.version_control.ignore import (
    VersionControllerIgnoreConfigFile as BaseVersionControllerIgnoreConfigFile,
)


class VersionControllerIgnoreConfigFile(BaseVersionControllerIgnoreConfigFile):
    """You can override methods from the base class to customize behavior."""

    def additional_ignore_lines(self) -> list[str]:
        """Add additional lines to ignore by version control."""
        return [*super().additional_ignore_lines(), "coverage.xml"]
