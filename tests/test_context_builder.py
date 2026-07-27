import json

from app.context.builder import build_replanning_context
from app.schemas.agent import (
    InvestigationPlan,
    PlanExecutionState,
    PlanStep,
    StepExecution,
)


def test_build_replanning_context():
    step = PlanStep(
        step_number=1,
        description="Inspect application logs.",
        expected_outcome="Find relevant errors.",
    )

    plan = InvestigationPlan(
        goal="Determine incident root cause.",
        steps=[step],
    )

    state = PlanExecutionState(
        plan=plan,
        completed_steps=[
            StepExecution(
                step=step,
                tool_name="query_logs",
                observation={
                    "error": "connection pool exhausted",
                },
                success=True,
            )
        ],
    )

    context = build_replanning_context(
        state
    )

    data = json.loads(context)

    assert data["current_goal"] == (
        "Determine incident root cause."
    )

    assert len(data["current_plan"]) == 1
    assert len(data["completed_steps"]) == 1

    assert (
        data["completed_steps"][0]["tool_name"]
        == "query_logs"
    )

    assert (
        data["completed_steps"][0]["observation"]["error"]
        == "connection pool exhausted"
    )