from app.context.builder import build_replanning_context
from app.llm.client import generate_revised_plan
from app.schemas.agent import (
    InvestigationPlan,
    PlanExecutionState,
)
from app.tools.registry import TOOL_REGISTRY


def should_replan(
    state: PlanExecutionState,
) -> bool:
    if not state.completed_steps:
        return False

    latest_execution = state.completed_steps[-1]

    return not latest_execution.success


def replan_investigation(
    state: PlanExecutionState,
    incident: str,
    service: str,
) -> InvestigationPlan:
    replanning_context = build_replanning_context(
        state
    )

    available_tools = [
        {
            "name": tool.name,
            "description": tool.description,
        }
        for tool in TOOL_REGISTRY.values()
    ]

    return generate_revised_plan(
        incident=incident,
        service=service,
        replanning_context=replanning_context,
        available_tools=available_tools,
    )