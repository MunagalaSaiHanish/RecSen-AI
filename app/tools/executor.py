from app.schemas.agent import AgentAction
from app.tools.investigation import (
    check_deployments,
    query_logs,
    query_metrics,
)


def execute_action(action: AgentAction, service: str) -> dict:
    if action == AgentAction.CHECK_LOGS:
        return query_logs(service)

    if action == AgentAction.CHECK_METRICS:
        return query_metrics(service)

    if action == AgentAction.CHECK_DEPLOYMENTS:
        return check_deployments(service)

    if action == AgentAction.FINISH:
        return {
            "service": service,
            "message": "Investigation finished.",
        }

    raise ValueError(f"Unsupported action: {action}")