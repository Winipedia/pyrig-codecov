"""Test module."""

from pyrig.core.resources import resource_content
from pyrig.core.strings import read_text_utf8

from pyrig_codecov.rig import resources
from pyrig_codecov.rig.configs.version_control.remote.workflows.health_check import (
    HealthCheckWorkflowConfigFile,
)


class TestHealthCheckWorkflowConfigFile:
    """Test class."""

    def test_steps_matrix_health_checks(self) -> None:
        """Test method."""
        last_step = HealthCheckWorkflowConfigFile.I.steps_matrix_health_checks()[-1]
        assert last_step["id"] == "upload-coverage-report"

    def test_codecov_action(self) -> None:
        """Test method."""
        assert HealthCheckWorkflowConfigFile.I.codecov_action() == tuple(
            resource_content("CODECOV_ACTION", resources).splitlines(),
        )

        action, ref, tag = HealthCheckWorkflowConfigFile.I.codecov_action()
        assert f'"uses": "{action}@{ref}"  # {tag}' in read_text_utf8(
            HealthCheckWorkflowConfigFile.I.path(),
        )

    def test_step_upload_coverage_report(self) -> None:
        """Test method."""
        step = HealthCheckWorkflowConfigFile.I.step_upload_coverage_report()
        assert isinstance(step, dict)
        assert "id" in step
        assert "name" in step
        assert "uses" in step
        assert "with" in step

    def test_insert_codecov_token(self) -> None:
        """Test method."""
        assert (
            HealthCheckWorkflowConfigFile.I.insert_codecov_token()
            == "${{ secrets.CODECOV_TOKEN }}"
        )

    def test_codecov_token_var(self) -> None:
        """Test method."""
        assert (
            HealthCheckWorkflowConfigFile.I.codecov_token_var()
            == "secrets.CODECOV_TOKEN"
        )
