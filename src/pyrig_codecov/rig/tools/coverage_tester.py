"""Coverage testing wrapper for the code coverage tool.

Wraps CoverageTester commands and information.
"""

from pathlib import Path

from pyrig.rig.tools.coverage_tester import CoverageTester as BaseCoverageTester
from pyrig.rig.tools.package_manager import PackageManager
from pyrig.rig.tools.version_control.version_controller import VersionController


class CoverageTester(BaseCoverageTester):
    """Overrides the base CoverageTester from pyrig."""

    def badge_urls(self) -> tuple[str, str]:
        """Get the Codecov badge image URL and dashboard URL.

        The badge image URL points to an SVG coverage badge on Codecov's CDN
        scoped to the default branch. The dashboard URL is the Codecov project
        page for the current repository.

        Returns:
            Tuple of (badge_image_url, dashboard_url), where badge_image_url
            is the SVG badge URL including the default branch, and dashboard_url
            is the Codecov project dashboard URL.
        """
        return (
            f"{self.remote_coverage_url()}/branch/{VersionController.I.default_branch()}/graph/badge.svg",
            self.remote_coverage_url(),
        )

    def version_control_ignore_paths(self) -> tuple[str, ...]:
        """Get the paths to ignore for version control."""
        return (*super().version_control_ignore_paths(), self.report_file().as_posix())

    def threshold(self) -> int:
        """Enforcing 100% coverage for packages with this plugin."""
        return 100

    def remote_coverage_url(self) -> str:
        """Construct the Codecov project dashboard URL for the current repository.

        Resolves the repository owner from the git remote and
        the repository name from the project name.

        Returns:
            URL in the format ``https://codecov.io/gh/{owner}/{repo}``.
        """
        owner, repo = (
            VersionController.I.repo_owner(check_repo_url=False),
            PackageManager.I.project_name(),
        )
        return f"https://codecov.io/gh/{owner}/{repo}"

    def access_token_key(self) -> str:
        """Get the environment variable name for the Codecov upload token.

        This key is referenced in CI workflow definitions to inject the
        Codecov authentication token when uploading coverage reports.

        Returns:
            'CODECOV_TOKEN'
        """
        return "CODECOV_TOKEN"

    def additional_args(self) -> tuple[str, ...]:
        """Get additional pytest-cov arguments for CI test runs.

        Added on top of ``additional_args()`` during CI execution to produce an
        XML coverage report, which is required for uploading results to Codecov.

        Returns:
            Tuple containing ``--cov-report=xml``.
        """
        return (
            *super().additional_args(),
            f"--cov-report={self.report_file().suffix.removeprefix('.')}",
        )

    def report_file(self) -> Path:
        """Get the Path object for the coverage report file.

        Returns:
            Path object pointing to the coverage report file
        """
        return Path("coverage.xml")
