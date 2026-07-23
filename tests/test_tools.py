from app.schemas.agent import AgentAction
from app.tools.executor import execute_action


def test_execute_logs_action():
    result = execute_action(
        AgentAction.CHECK_LOGS,
        "payment-api",
    )

    assert result["service"] == "payment-api"
    assert len(result["logs"]) > 0


def test_execute_metrics_action():
    result = execute_action(
        AgentAction.CHECK_METRICS,
        "payment-api",
    )

    assert result["cpu_usage"] == 91
    assert result["error_rate"] == 17


def test_execute_deployment_action():
    result = execute_action(
        AgentAction.CHECK_DEPLOYMENTS,
        "payment-api",
    )

    assert result["version"] == "2.4.1"