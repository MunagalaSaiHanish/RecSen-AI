from app.agents.executor import execute_plan_step
from app.agents.replanner import (
    replan_investigation,
    should_replan,
)
from app.schemas.agent import (
    InvestigationPlan,
    PlanExecutionState,
)


def execute_plan(
    plan: InvestigationPlan,
    incident: str,
    service: str,
) -> PlanExecutionState:
    state = PlanExecutionState(
        plan=plan,
    )

    current_plan = plan

    for step in current_plan.steps:
        execution = execute_plan_step(
            step=step,
            service=service,
        )

        state.completed_steps.append(
            execution
        )

        if should_replan(state):
            new_plan = replan_investigation(
                state=state,
                incident=incident,
                service=service,
            )

            state.plan = new_plan

            break

    return state