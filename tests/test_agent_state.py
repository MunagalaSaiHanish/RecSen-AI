from app.schemas.agent import (
    AgentAction,
    AgentStatus,
    InvestigationPlan,
    InvestigationState,
    InvestigationStep,
    PlanExecutionState,
    PlanStep,
    
)
from app.schemas.agent import AgentStatus


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

def test_plan_execution_state_defaults():
    step = PlanStep(
        step_number=1,
        description="Inspect logs.",
        expected_outcome="Find relevant errors.",
    )

    plan = InvestigationPlan(
        goal="Investigate incident.",
        steps=[step],
    )

    state = PlanExecutionState(
        plan=plan,
    )

    assert state.status == AgentStatus.PLANNING
    assert state.current_step_index == 0
    assert state.replan_count == 0
    assert state.completed_steps == []