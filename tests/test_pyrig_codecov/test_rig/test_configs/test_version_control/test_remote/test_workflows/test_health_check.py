"""Test module."""

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
        result = HealthCheckWorkflowConfigFile.I.codecov_action()
        assert isinstance(result, str)
        assert result

    def test_codecov_action_sha(self) -> None:
        """Test method."""
        result = HealthCheckWorkflowConfigFile.I.codecov_action_sha()
        assert isinstance(result, str)
        assert result

    def test_step_upload_coverage_report(self) -> None:
        """Test method."""
        action = HealthCheckWorkflowConfigFile.I.codecov_action()
        sha = HealthCheckWorkflowConfigFile.I.codecov_action_sha()
        assert HealthCheckWorkflowConfigFile.I.step_upload_coverage_report() == {
            "id": "upload-coverage-report",
            "name": "Upload Coverage Report",
            "uses": f"{action}@{sha}",
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
