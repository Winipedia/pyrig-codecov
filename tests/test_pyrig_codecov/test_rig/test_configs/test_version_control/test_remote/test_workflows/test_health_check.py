"""Test module."""

from pathlib import Path

from pyrig.core.resources import resource_content
from pyrig.core.strings import read_text_utf8

from pyrig_codecov.rig import resources
from pyrig_codecov.rig.configs.version_control.remote.workflows.health_check import (
    HealthCheckWorkflowConfigFile,
)


class TestHealthCheckWorkflowConfigFile:
    """Test class."""

    def test_action_codecov(self) -> None:
        """Test method."""
        assert HealthCheckWorkflowConfigFile.I.action_codecov() == tuple(
            resource_content("ACTION_CODECOV", resources).splitlines(),
        )

        action, ref, tag = HealthCheckWorkflowConfigFile.I.action_codecov()
        assert f'"uses": "{action}@{ref}"  # {tag}' in read_text_utf8(
            HealthCheckWorkflowConfigFile.I.path(),
        )

    def test_artifact_name(self) -> None:
        """Test method."""
        workflow = HealthCheckWorkflowConfigFile.I
        assert workflow.artifact_name("ubuntu-latest", "3.12") == (
            "coverage-ubuntu-latest-3.12"
        )

    def test_coverage_reports_dir(self) -> None:
        """Test method."""
        assert HealthCheckWorkflowConfigFile.I.coverage_reports_dir() == Path(
            "coverage-reports",
        )

    def test_job_health_check_needs(self) -> None:
        """Test method."""
        workflow = HealthCheckWorkflowConfigFile.I
        assert workflow.job_health_check_needs() == (
            *super(HealthCheckWorkflowConfigFile, workflow).job_health_check_needs(),
            workflow.job_upload_coverage,
        )

    def test_job_upload_coverage(self) -> None:
        """Test method."""
        workflow = HealthCheckWorkflowConfigFile.I
        job = workflow.job_upload_coverage()
        assert job["needs"] == ["matrix-health-checks"]
        assert job["runs-on"] == "ubuntu-latest"
        assert job["timeout-minutes"] == 30  # noqa: PLR2004
        assert "strategy" not in job
        assert job["permissions"] == workflow.job_upload_coverage_permissions()
        assert job["steps"] == workflow.steps_upload_coverage()

    def test_job_upload_coverage_permissions(self) -> None:
        """Test method."""
        assert HealthCheckWorkflowConfigFile.I.job_upload_coverage_permissions() == {
            "id-token": "write",
        }

    def test_jobs(self) -> None:
        """Test method."""
        workflow = HealthCheckWorkflowConfigFile.I
        jobs = workflow.jobs()
        index = jobs.index(workflow.job_matrix_health_checks) + 1
        assert jobs[index] == workflow.job_upload_coverage
        assert (
            jobs[:index] + jobs[index + 1 :]
            == super(
                HealthCheckWorkflowConfigFile,
                workflow,
            ).jobs()
        )

    def test_step_download_coverage_reports(self) -> None:
        """Test method."""
        workflow = HealthCheckWorkflowConfigFile.I
        step = workflow.step_download_coverage_reports()
        action, ref, _ = workflow.action_download_artifact()
        assert step["uses"] == f"{action}@{ref}"
        assert step["with"] == {
            "pattern": "coverage-*-*",
            "path": "coverage-reports",
            "merge-multiple": "false",
        }

    def test_step_upload_coverage(self) -> None:
        """Test method."""
        step = HealthCheckWorkflowConfigFile.I.step_upload_coverage()
        assert isinstance(step, dict)
        assert "id" in step
        assert "name" in step
        assert "uses" in step
        assert "with" in step
        assert step["with"] == {
            "directory": "coverage-reports",
            "fail_ci_if_error": "true",
            "use_oidc": "true",
        }

    def test_step_upload_coverage_report(self) -> None:
        """Test method."""
        workflow = HealthCheckWorkflowConfigFile.I
        step = workflow.step_upload_coverage_report()
        action, ref, _ = workflow.action_upload_artifact()
        assert step["uses"] == f"{action}@{ref}"
        assert step["with"] == {
            "name": "coverage-${{ matrix.os }}-${{ matrix.python-version }}",
            "path": "coverage.xml",
            "if-no-files-found": "error",
        }

    def test_steps_matrix_health_checks(self) -> None:
        """Test method."""
        workflow = HealthCheckWorkflowConfigFile.I
        steps = workflow.steps_matrix_health_checks()
        base_steps = super(
            HealthCheckWorkflowConfigFile,
            workflow,
        ).steps_matrix_health_checks()
        assert steps == [
            *base_steps,
            workflow.step_upload_coverage_report(),
        ]
        assert not any(
            step.get("uses", "").startswith("codecov/codecov-action@") for step in steps
        )

    def test_steps_upload_coverage(self) -> None:
        """Test method."""
        workflow = HealthCheckWorkflowConfigFile.I
        steps = workflow.steps_upload_coverage()
        assert steps == [
            workflow.step_download_coverage_reports(),
            workflow.step_upload_coverage(),
        ]
        assert all("uses" in step and "run" not in step for step in steps)

    def test_workflow_file(self) -> None:
        """Test method."""
        jobs = HealthCheckWorkflowConfigFile.I.load()["jobs"]
        job_ids = list(jobs)
        assert job_ids[job_ids.index("matrix-health-checks") + 1] == "upload-coverage"
        assert jobs["matrix-health-checks"]["permissions"] == {"contents": "read"}
        assert jobs["matrix-health-checks"]["steps"][-1]["id"] == (
            "upload-coverage-report"
        )
        assert (
            jobs["upload-coverage"]
            == HealthCheckWorkflowConfigFile.I.job_by_id(
                HealthCheckWorkflowConfigFile.I.job_upload_coverage,
            )["upload-coverage"]
        )
        assert "upload-coverage" in jobs["health-check"]["needs"]
