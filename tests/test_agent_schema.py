import pytest
from pydantic import ValidationError

from app.schemas.agent import AgentAction, AgentDecision


def test_valid_agent_decision():
    decision = AgentDecision(
        action=AgentAction.CHECK_LOGS,
        reason="Logs may reveal the source of the HTTP 500 errors.",
    )

    assert decision.action == AgentAction.CHECK_LOGS
    assert decision.reason != ""


def test_invalid_agent_action():
    with pytest.raises(ValidationError):
        AgentDecision(
            action="FLY_TO_MARS",
            reason="This action does not exist.",
        )