from app.agents.executor import execute_plan_step
from app.agents.replanner import (
    replan_investigation,
    should_replan,
)
from app.schemas.agent import (
    AgentStatus,
    InvestigationPlan,
    PlanExecutionState,
)


MAX_REPLANS = 3


def execute_plan(
    plan: InvestigationPlan,
    incident: str,
    service: str,
) -> PlanExecutionState:
    state = PlanExecutionState(
        plan=plan,
    )

    state.status = AgentStatus.EXECUTING

    while state.status not in {
        AgentStatus.COMPLETED,
        AgentStatus.FAILED,
    }:
        if state.current_step_index >= len(
            state.plan.steps
        ):
            state.status = AgentStatus.COMPLETED
            continue

        step = state.plan.steps[
            state.current_step_index
        ]

        execution = execute_plan_step(
            step=step,
            service=service,
        )

        state.completed_steps.append(
            execution
        )

        state.status = AgentStatus.EVALUATING

        if should_replan(state):
            if state.replan_count >= MAX_REPLANS:
                state.status = AgentStatus.FAILED
                continue

            state.status = AgentStatus.REPLANNING

            new_plan = replan_investigation(
                state=state,
                incident=incident,
                service=service,
            )

            state.plan = new_plan
            state.current_step_index = 0
            state.replan_count += 1
            state.status = AgentStatus.EXECUTING

            continue

        state.current_step_index += 1
        state.status = AgentStatus.EXECUTING

    return state