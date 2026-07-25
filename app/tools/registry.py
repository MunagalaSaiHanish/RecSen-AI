from app.schemas.tools import ServiceToolInput
from app.tools.base import Tool
from app.tools.investigation import (
    check_deployments,
    query_logs,
    query_metrics,
)


TOOL_REGISTRY: dict[str, Tool] = {
    "query_logs": Tool(
        name="query_logs",
        description=(
            "Retrieve recent application error logs for a service."
        ),
        input_model=ServiceToolInput,
        function=query_logs,
    ),
    "query_metrics": Tool(
        name="query_metrics",
        description=(
            "Retrieve runtime metrics for a service."
        ),
        input_model=ServiceToolInput,
        function=query_metrics,
    ),
    "check_deployments": Tool(
        name="check_deployments",
        description=(
            "Retrieve recent deployment information for a service."
        ),
        input_model=ServiceToolInput,
        function=check_deployments,
    ),
}