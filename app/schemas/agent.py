from enum import Enum

from pydantic import BaseModel, Field


class AgentAction(str, Enum):
    CHECK_LOGS = "CHECK_LOGS"
    CHECK_METRICS = "CHECK_METRICS"
    CHECK_DEPLOYMENTS = "CHECK_DEPLOYMENTS"
    FINISH = "FINISH"


class AgentDecision(BaseModel):
    action: AgentAction
    reason: str = Field(min_length=1)