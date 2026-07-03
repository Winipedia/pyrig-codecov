"""Codecov integration for the health check CI workflow."""

from typing import Any

from pyrig.rig.configs.version_control.remote.workflows.health_check import (
    HealthCheckWorkflowConfigFile as BaseHealthCheckWorkflowConfigFile,
)

from pyrig_codecov.rig.tools.testers.coverage import CoverageTester


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

    def step_upload_coverage_report(
        self,
        *,
        step: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Build a step that uploads the coverage report to Codecov.

        Fails the CI job if the upload fails.

        Args:
            step: Additional keys to merge into the step configuration.

        Returns:
            Step using `codecov/codecov-action@main`.

        Note:
            Requires a Codecov account linked to the repository (log in at
            codecov.io with GitHub).
        """
        return self.step(
            self.step_upload_coverage_report,
            uses="codecov/codecov-action@main",
            with_={
                "files": CoverageTester.I.report_file().as_posix(),
                "token": self.insert_codecov_token(),
                "fail_ci_if_error": "true",
                "skip_validation": "true",
            },
            step=step,
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
        return self.secrets_var(CoverageTester.I.access_token_key())
