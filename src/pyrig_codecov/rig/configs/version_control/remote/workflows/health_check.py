"""Codecov coverage-upload step for the health check CI workflow."""

from typing import Any

from pyrig.core.resources import resource_content
from pyrig.rig.configs.version_control.remote.workflows.health_check import (
    HealthCheckWorkflowConfigFile as BaseHealthCheckWorkflowConfigFile,
)

from pyrig_codecov.rig import resources
from pyrig_codecov.rig.tools.testing.project import ProjectTester


class HealthCheckWorkflowConfigFile(BaseHealthCheckWorkflowConfigFile):
    """Health check workflow extended with a Codecov coverage upload step."""

    def steps_matrix_health_checks(self) -> list[dict[str, Any]]:
        """Return the matrix job steps, extended with a Codecov upload step.

        Returns:
            The base class steps plus a final step that uploads the
            coverage report to Codecov.
        """
        return [
            *super().steps_matrix_health_checks(),
            self.step_upload_coverage_report(),
        ]

    def codecov_action_ref(self) -> str:
        """Return the pinned commit SHA for `codecov/codecov-action`.

        Returns:
            Commit SHA `codecov/codecov-action` is pinned to.
        """
        return resource_content(
            self.codecov_action_ref.__name__.upper(),
            resources,
        ).strip()

    def step_upload_coverage_report(self) -> dict[str, Any]:
        """Build a step that uploads the coverage report to Codecov.

        Fails the CI job if the upload fails.

        Returns:
            Step using `codecov/codecov-action@<sha>`.

        Note:
            The upload token always comes from a `CODECOV_TOKEN` repository
            secret, so it must be configured for the upload to succeed.
        """
        return self.step(
            self.step_upload_coverage_report,
            uses=(
                "codecov/codecov-action",
                self.codecov_action_ref(),
            ),
            with_={
                "files": ProjectTester.I.report_file().as_posix(),
                "token": self.insert_codecov_token(),
                "fail_ci_if_error": "true",
                "skip_validation": "true",
            },
        )

    def insert_codecov_token(self) -> str:
        """Return the `${{ secrets.CODECOV_TOKEN }}` expression.

        Returns:
            GitHub Actions expression for the `CODECOV_TOKEN` secret.
        """
        return self.insert_expression(self.codecov_token_var())

    def codecov_token_var(self) -> str:
        """Return the raw secrets expression for `CODECOV_TOKEN`.

        Returns:
            The `"secrets.CODECOV_TOKEN"` expression string.
        """
        return self.secrets_var(ProjectTester.I.access_token_key())
