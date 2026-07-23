from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class AgentAction(str, Enum):
    CHECK_LOGS = "CHECK_LOGS"
    CHECK_METRICS = "CHECK_METRICS"
    CHECK_DEPLOYMENTS = "CHECK_DEPLOYMENTS"
    FINISH = "FINISH"


class AgentDecision(BaseModel):
    action: AgentAction
    reason: str = Field(min_length=1)


class InvestigationStep(BaseModel):
    action: AgentAction
    reason: str = Field(min_length=1)
    observation: dict[str, Any]


class InvestigationState(BaseModel):
    incident: str
    service: str
    steps: list[InvestigationStep] = Field(default_factory=list)
    finished: bool = False