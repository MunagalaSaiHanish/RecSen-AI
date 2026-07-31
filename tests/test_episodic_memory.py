from app.memory.episodic_memory import create_episode
from app.schemas.agent import (
    InvestigationPlan,
    PlanExecutionState,
    PlanStep,
)


def test_create_episode():
    plan = InvestigationPlan(
        goal="Investigate payment-api",
        reasoning="Testing episode creation.",
        steps=[
            PlanStep(
                step_number=1,
                description="Inspect logs",
                expected_outcome="Find root cause",
            )
        ],
    )

    state = PlanExecutionState(
        plan=plan,
    )

    episode = create_episode(
        incident="payment-api",
        execution_state=state,
    )

    assert episode.incident == "payment-api"
    assert episode.completed_steps == []