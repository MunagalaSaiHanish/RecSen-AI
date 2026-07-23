from app.agents.incident_agent import decide_next_action
from app.schemas.agent import (
    AgentAction,
    InvestigationState,
    InvestigationStep,
)
from app.tools.executor import execute_action


MAX_STEPS = 5


def run_investigation(
    incident: str,
    service: str,
) -> InvestigationState:
    state = InvestigationState(
        incident=incident,
        service=service,
    )

    for _ in range(MAX_STEPS):
        decision = decide_next_action(state)

        if decision.action == AgentAction.FINISH:
            state.finished = True
            break

        observation = execute_action(
            action=decision.action,
            service=state.service,
        )

        step = InvestigationStep(
            action=decision.action,
            reason=decision.reason,
            observation=observation,
        )

        state.steps.append(step)

    return state