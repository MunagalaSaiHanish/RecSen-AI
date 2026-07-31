from app.memory.episode_builder import build_episode

from app.schemas.agent import (
    Episode,
    InvestigationPlan,
    InvestigationRecord,
    PlanExecutionState,
    PlanStep,
)


def test_build_episode():

    plan = InvestigationPlan(
        goal="Investigate Payment API",
        reasoning="Testing",
        steps=[
            PlanStep(
                step_number=1,
                description="Inspect Logs",
                expected_outcome="Find issue",
            )
        ],
    )

    state = PlanExecutionState(
        plan=plan,
    )

    episode = build_episode(
        incident="payment-api",
        execution_state=state,
    )

    assert isinstance(
        episode,
        Episode,
    )

    assert (
        episode.investigation.incident
        ==
        "payment-api"
    )