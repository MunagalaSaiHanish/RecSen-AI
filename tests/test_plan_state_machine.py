from unittest.mock import patch

from app.agents.plan_executor import execute_plan
from app.schemas.agent import (
    AgentStatus,
    InvestigationPlan,
    PlanStep,
    StepExecution,
)


def create_plan():
    return InvestigationPlan(
        goal="Investigate payment-api incident.",
        steps=[
            PlanStep(
                step_number=1,
                description="Inspect logs.",
                expected_outcome="Find errors.",
            ),
            PlanStep(
                step_number=2,
                description="Inspect metrics.",
                expected_outcome="Find anomalies.",
            ),
        ],
    )


@patch(
    "app.agents.plan_executor.execute_plan_step"
)
def test_successful_plan_reaches_completed(
    mock_execute,
):
    plan = create_plan()

    mock_execute.side_effect = [
        StepExecution(
            step=plan.steps[0],
            tool_name="query_logs",
            observation={},
            success=True,
        ),
        StepExecution(
            step=plan.steps[1],
            tool_name="query_metrics",
            observation={},
            success=True,
        ),
    ]

    state = execute_plan(
        plan=plan,
        incident="HTTP 500 errors",
        service="payment-api",
    )

    assert state.status == AgentStatus.COMPLETED
    assert len(state.completed_steps) == 2
    assert state.current_step_index == 2
    assert state.replan_count == 0