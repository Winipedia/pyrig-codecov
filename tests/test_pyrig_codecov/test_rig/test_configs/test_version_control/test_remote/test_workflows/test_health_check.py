"""Test module."""

from pyrig.core.resources import resource_content

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

    def test_codecov_action_ref(self) -> None:
        """Test method."""
        assert HealthCheckWorkflowConfigFile.I.codecov_action_ref() == (
            resource_content("CODECOV_ACTION_REF", resources).strip()
        )

    def test_step_upload_coverage_report(self) -> None:
        """Test method."""
        assert HealthCheckWorkflowConfigFile.I.step_upload_coverage_report() == {
            "id": "upload-coverage-report",
            "name": "Upload Coverage Report",
            "uses": (
                "codecov/codecov-action@"
                f"{HealthCheckWorkflowConfigFile.I.codecov_action_ref()}"
            ),
            "with": {
                "files": "coverage.xml",
                "token": "${{ secrets.CODECOV_TOKEN }}",  # nosec: B105
                "fail_ci_if_error": "true",
                "skip_validation": "true",
            },
        }

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
