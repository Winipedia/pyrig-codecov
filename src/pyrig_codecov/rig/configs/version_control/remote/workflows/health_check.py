"""Generate a health-check workflow that uploads matrix coverage to Codecov."""

from collections.abc import Callable
from pathlib import Path
from types import MethodType
from typing import Any, override

from pyrig.rig.configs.version_control.remote.workflows.health_check import (
    HealthCheckWorkflowConfigFile as BaseHealthCheckWorkflowConfigFile,
)

from pyrig_codecov.rig import resources
from pyrig_codecov.rig.tools.testing.project import ProjectTester


class HealthCheckWorkflowConfigFile(BaseHealthCheckWorkflowConfigFile):
    """Store matrix reports and upload them to Codecov in a separate job."""

    @override
    def job_health_check_needs(self) -> tuple[MethodType, ...]:
        """Wait for coverage publishing before the aggregate job runs."""
        return (*super().job_health_check_needs(), self.job_upload_coverage)

    @override
    def jobs(self) -> tuple[Callable[[], dict[str, Any]], ...]:
        """Place the upload job after the matrix test job."""
        jobs = list(super().jobs())
        jobs.insert(
            jobs.index(self.job_matrix_health_checks) + 1,
            self.job_upload_coverage,
        )
        return tuple(jobs)

    @override
    def steps_matrix_health_checks(self) -> list[dict[str, Any]]:
        """Add coverage artifact storage after the matrix test steps."""
        return [
            *super().steps_matrix_health_checks(),
            self.step_upload_coverage_report(),
        ]

    def job_upload_coverage(self) -> dict[str, Any]:
        """Build the OIDC-enabled job that uploads matrix reports to Codecov."""
        return self.job(
            self.job_upload_coverage,
            needs=(self.job_matrix_health_checks,),
            permissions=self.job_upload_coverage_permissions(),
            steps=self.steps_upload_coverage(),
            timeout_minutes=30,
        )

    def step_upload_coverage_report(self) -> dict[str, Any]:
        """Store this matrix job's coverage XML as an artifact.

        Fail if the coverage report file is missing.
        """
        return self.step_upload_artifact(
            self.step_upload_coverage_report,
            name=self.artifact_name(
                self.insert_matrix_os(),
                self.insert_matrix_python_version(),
            ),
            path=ProjectTester.I.report_file(),
        )

    def job_upload_coverage_permissions(self) -> dict[str, Any]:
        """Return the OIDC token permission required by Codecov."""
        return self.permission_id_token(write=True)

    def steps_upload_coverage(self) -> list[dict[str, Any]]:
        """Download and upload reports."""
        return [
            self.step_download_coverage_reports(),
            self.step_upload_coverage(),
        ]

    def step_download_coverage_reports(self) -> dict[str, Any]:
        """Download this run's reports into separate artifact directories.

        Separate directories prevent identically named reports from overwriting.
        """
        return self.step_download_artifact(
            self.step_download_coverage_reports,
            pattern=self.artifact_name("*", "*"),
            path=self.coverage_reports_dir(),
            merge_multiple=False,
        )

    def step_upload_coverage(self) -> dict[str, Any]:
        """Upload reports from the artifact directory using OIDC.

        Fail the job if the upload fails.
        """
        return self.step(
            self.step_upload_coverage,
            uses=self.action_codecov(),
            with_={
                "directory": self.coverage_reports_dir().as_posix(),
                "fail_ci_if_error": "true",
                "use_oidc": "true",
            },
        )

    def action_codecov(self) -> tuple[str, str, str]:
        """Return the name, pinned commit SHA, and release tag for Codecov.

        Returns:
            Metadata for `codecov/codecov-action`.
        """
        return self.action_from_resource(self.action_codecov, resources)

    def artifact_name(self, os: str, python_version: str) -> str:
        """Return a name identifying a matrix OS and Python version."""
        return f"coverage-{os}-{python_version}"

    def coverage_reports_dir(self) -> Path:
        """Return the directory containing downloaded coverage artifacts."""
        return Path("coverage-reports")
