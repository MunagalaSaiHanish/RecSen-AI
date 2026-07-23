from app.schemas.agent import (
    AgentAction,
    InvestigationState,
    InvestigationStep,
)


def test_initial_investigation_state():
    state = InvestigationState(
        incident="Payment API is failing.",
        service="payment-api",
    )

    assert state.incident == "Payment API is failing."
    assert state.service == "payment-api"
    assert state.steps == []
    assert state.finished is False


def test_add_investigation_step():
    state = InvestigationState(
        incident="Payment API is failing.",
        service="payment-api",
    )

    step = InvestigationStep(
        action=AgentAction.CHECK_LOGS,
        reason="Inspect the errors.",
        observation={
            "logs": ["Database timeout"]
        },
    )

    state.steps.append(step)

    assert len(state.steps) == 1
    assert state.steps[0].action == AgentAction.CHECK_LOGS