"""Test module."""

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

    def test_job_matrix_health_checks_permissions(self) -> None:
        """Test method."""
        assert (
            HealthCheckWorkflowConfigFile.I.job_matrix_health_checks_permissions()
            == {
                "contents": "read",
                "id-token": "write",
            }
        )

    def test_step_upload_coverage_report(self) -> None:
        """Test method."""
        step = HealthCheckWorkflowConfigFile.I.step_upload_coverage_report()
        assert isinstance(step, dict)
        assert "id" in step
        assert "name" in step
        assert "uses" in step
        assert "with" in step
        assert step["with"]["use_oidc"] == "true"
        assert "token" not in step["with"]

    def test_steps_matrix_health_checks(self) -> None:
        """Test method."""
        last_step = HealthCheckWorkflowConfigFile.I.steps_matrix_health_checks()[-1]
        assert last_step["id"] == "upload-coverage-report"
