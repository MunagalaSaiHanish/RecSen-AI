from app.agents.replanner import should_replan
from app.schemas.agent import (
    InvestigationPlan,
    PlanExecutionState,
    PlanStep,
    StepExecution,
)


def create_test_plan():
    return InvestigationPlan(
        goal="Determine incident root cause.",
        steps=[
            PlanStep(
                step_number=1,
                description="Inspect logs.",
                expected_outcome="Find relevant errors.",
            )
        ],
    )


def test_successful_step_does_not_trigger_replanning():
    plan = create_test_plan()

    state = PlanExecutionState(
        plan=plan,
        completed_steps=[
            StepExecution(
                step=plan.steps[0],
                tool_name="query_logs",
                observation={},
                success=True,
            )
        ],
    )

    assert should_replan(state) is False


def test_failed_step_triggers_replanning():
    plan = create_test_plan()

    state = PlanExecutionState(
        plan=plan,
        completed_steps=[
            StepExecution(
                step=plan.steps[0],
                tool_name="query_logs",
                observation=None,
                success=False,
            )
        ],
    )

    assert should_replan(state) is True


def test_empty_execution_does_not_trigger_replanning():
    plan = create_test_plan()

    state = PlanExecutionState(
        plan=plan,
    )

    assert should_replan(state) is False