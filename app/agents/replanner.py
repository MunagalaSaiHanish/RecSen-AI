from app.agents.planner import create_investigation_plan
from app.schemas.agent import (
    InvestigationPlan,
    PlanExecutionState,
)


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
    return create_investigation_plan(
        incident=incident,
        service=service,
    )