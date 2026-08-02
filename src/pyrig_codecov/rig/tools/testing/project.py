"""Codecov-specific coverage reporting and badge configuration."""

from pathlib import Path

from pyrig.core.subprocesses import Args
from pyrig.rig.tools.packages.manager import PackageManager
from pyrig.rig.tools.testing.project import ProjectTester as BaseProjectTester
from pyrig.rig.tools.version_control.controller import VersionController


class ProjectTester(BaseProjectTester):
    """Coverage tool configured for Codecov as the reporting backend.

    Points the coverage badge at Codecov instead of a static shields.io
    badge, raises the required coverage threshold to 100%, and exposes the
    report file, format, and upload token needed to publish results to
    Codecov from CI.
    """

    def additional_args(self) -> Args:
        """Return the base pytest flags, extended with a report-format flag.

        Returns:
            The base pytest flags plus a `--cov-report`
            flag set to `report_format()`'s value.
        """
        return Args(
            *super().additional_args(),
            f"--cov-report={self.report_format()}",
        )

    def image_url(self) -> str:
        """Return the URL of the Codecov coverage badge image for the default branch."""
        remote_url, branch = (
            self.link_url(),
            VersionController.I.default_branch(),
        )
        return f"{remote_url}/branch/{branch}/graph/badge.svg"

    def link_url(self) -> str:
        """Return the URL of the Codecov project dashboard."""
        owner, repo = (
            VersionController.I.repo_owner(),
            PackageManager.I.project_name(),
        )
        return f"https://codecov.io/gh/{owner}/{repo}"

    def threshold(self) -> int:
        """Return `100`."""
        return 100

    def version_control_ignore_patterns(self) -> tuple[str, ...]:
        """Return the base ignore paths plus the coverage report file."""
        return (
            *super().version_control_ignore_patterns(),
            self.report_file().as_posix(),
        )

    def access_token_key(self) -> str:
        """Return `'CODECOV_TOKEN'`, the env var name for the Codecov upload token."""
        return "CODECOV_TOKEN"

    def report_file(self) -> Path:
        """Return the coverage report file path.

        Returns:
            `coverage.<ext>`, where `<ext>` is `report_format()`'s value.
        """
        return Path(f"coverage.{self.report_format()}")

    def report_format(self) -> str:
        """Return `'xml'`, the coverage report format."""
        return "xml"
