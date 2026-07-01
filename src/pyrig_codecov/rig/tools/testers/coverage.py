"""Coverage testing wrapper for the code coverage tool.

Wraps CoverageTester commands and information.
"""

from pathlib import Path

from pyrig.core.subprocesses import Args
from pyrig.rig.tools.package_manager import PackageManager
from pyrig.rig.tools.testers.coverage import CoverageTester as BaseCoverageTester
from pyrig.rig.tools.version_control.version_controller import VersionController


class CoverageTester(BaseCoverageTester):
    """Overrides the base CoverageTester from pyrig."""

    def image_url(self) -> str:
        """Get the URL for the coverage badge image.

        Returns:
            URL string for the coverage badge image.
        """
        remote_url, branch = (
            self.remote_coverage_url(),
            VersionController.I.default_branch(),
        )
        return f"{remote_url}/branch/{branch}/graph/badge.svg"

    def link_url(self) -> str:
        """Get the URL for the coverage badge link.

        Returns:
            URL string for the coverage badge link, the Codecov project dashboard.
        """
        return self.remote_coverage_url()

    def version_control_ignore_paths(self) -> tuple[str, ...]:
        """Get the paths to ignore for version control."""
        return (*super().version_control_ignore_paths(), self.report_file().as_posix())

    def additional_test_args(self) -> Args:
        """Get pytest-cov arguments, extended with an XML coverage report.

        Extends the base arguments (added to ``[tool.pytest.ini_options] addopts``
        in ``pyproject.toml``, so they apply to every ``pytest`` invocation) with
        ``--cov-report=xml`` so that a ``coverage.xml`` report is produced on each
        test run. This report is required for uploading results to Codecov in CI.

        Returns:
            The base arguments plus ``--cov-report=xml``.
        """
        return Args(
            *super().additional_test_args(),
            f"--cov-report={self.report_file().suffix.removeprefix('.')}",
        )

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
            VersionController.I.repo_owner(),
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

    def report_file(self) -> Path:
        """Get the Path object for the coverage report file.

        Returns:
            Path object pointing to the coverage report file
        """
        return Path("coverage.xml")
