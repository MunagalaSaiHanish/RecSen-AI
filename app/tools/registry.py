from collections.abc import Callable

from app.tools.investigation import (
    check_deployments,
    query_logs,
    query_metrics,
)


TOOL_REGISTRY: dict[str, Callable] = {
    "query_logs": query_logs,
    "query_metrics": query_metrics,
    "check_deployments": check_deployments,
}