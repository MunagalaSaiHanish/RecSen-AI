import pytest
from pydantic import ValidationError

from app.schemas.agent import (
    InvestigationPlan,
    PlanStep,
)


def test_valid_investigation_plan():
    plan = InvestigationPlan(
        goal="Determine why payment-api is failing.",
        steps=[
            PlanStep(
                step_number=1,
                description="Inspect recent deployments.",
                expected_outcome=(
                    "Determine whether a deployment "
                    "correlates with the incident."
                ),
            ),
            PlanStep(
                step_number=2,
                description="Inspect application logs.",
                expected_outcome=(
                    "Identify errors related to the failure."
                ),
            ),
        ],
    )

    assert plan.goal == "Determine why payment-api is failing."
    assert len(plan.steps) == 2
    assert plan.steps[0].step_number == 1


def test_plan_requires_at_least_one_step():
    with pytest.raises(ValidationError):
        InvestigationPlan(
            goal="Determine the root cause.",
            steps=[],
        )


def test_step_number_must_be_positive():
    with pytest.raises(ValidationError):
        PlanStep(
            step_number=0,
            description="Inspect logs.",
            expected_outcome="Find relevant errors.",
        )