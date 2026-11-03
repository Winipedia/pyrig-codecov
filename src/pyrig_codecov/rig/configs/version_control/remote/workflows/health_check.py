"""Codecov coverage-upload step for the health check CI workflow."""

from typing import Any, override

from pyrig.rig.configs.version_control.remote.workflows.health_check import (
    HealthCheckWorkflowConfigFile as BaseHealthCheckWorkflowConfigFile,
)

from pyrig_codecov.rig import resources
from pyrig_codecov.rig.tools.testing.project import ProjectTester


class HealthCheckWorkflowConfigFile(BaseHealthCheckWorkflowConfigFile):
    """Health check workflow extended with a Codecov coverage upload step."""

    @override
    def job_matrix_health_checks_permissions(self) -> dict[str, Any]:
        """Return matrix-job permissions including Codecov OIDC upload access."""
        return {
            **super().job_matrix_health_checks_permissions(),
            **self.permission_id_token(write=True),
        }

    @override
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

    def step_upload_coverage_report(self) -> dict[str, Any]:
        """Build a step that uploads the coverage report to Codecov.

        Fails the CI job if the upload fails.

        Returns:
            Step using `codecov/codecov-action@<ref>`.

        Note:
            Uploads authenticate with GitHub OIDC instead of a repository
            secret.
        """
        return self.step(
            self.step_upload_coverage_report,
            uses=self.action_codecov(),
            with_={
                "files": ProjectTester.I.report_file().as_posix(),
                "fail_ci_if_error": "true",
                "skip_validation": "true",
                "use_oidc": "true",
            },
        )

    def action_codecov(self) -> tuple[str, str, str]:
        """Return action metadata for `codecov/codecov-action`.

        Returns:
            Tuple of action name, pinned commit SHA, and release tag.
        """
        return self.action_from_resource(self.action_codecov, resources)
