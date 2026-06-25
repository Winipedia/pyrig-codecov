"""GitHub Actions workflow generator for the health check CI stage."""

from typing import Any

from pyrig.rig.configs.version_control.remote.workflows.health_check import (
    HealthCheckWorkflowConfigFile as BaseHealthCheckWorkflowConfigFile,
)

from pyrig_codecov.rig.tools.testers.coverage import CoverageTester


class HealthCheckWorkflowConfigFile(BaseHealthCheckWorkflowConfigFile):
    """Overrides the base class methods to customize the health check workflow."""

    def steps_matrix_health_checks(self) -> list[dict[str, Any]]:
        """Return the steps for the matrix health checks job.

        Extends the base class steps with an additional step to upload the
        coverage report to Codecov.

        Returns:
            List of step configuration dicts for the matrix health checks job,
            including the Codecov upload step.
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

        Requires a Codecov account linked to the repository (log in at
        codecov.io with GitHub).
        Fails the CI job if the upload fails, ensuring that coverage reports are
        always uploaded when the health check workflow runs.

        Args:
            step: Additional keys to merge into the step configuration.

        Returns:
            Step using ``codecov/codecov-action@main``.
        """
        return self.step(
            step_func=self.step_upload_coverage_report,
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
        """Get the ``${{ secrets.CODECOV_TOKEN }}`` expression.

        Returns:
            GitHub Actions expression for the ``CODECOV_TOKEN`` secret.
        """
        return self.insert_expression(self.codecov_token_var())

    def codecov_token_var(self) -> str:
        """Get the raw secrets expression for ``CODECOV_TOKEN``.

        Returns:
            ``"secrets.CODECOV_TOKEN"``
        """
        return self.secrets_var(CoverageTester.I.access_token_key())
