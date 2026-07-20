from enum import Enum

from pydantic import BaseModel, Field


class AgentAction(str, Enum):
    QUERY_LOGS = "QUERY_LOGS"
    QUERY_METRICS = "QUERY_METRICS"
    CHECK_DEPLOYMENTS = "CHECK_DEPLOYMENTS"
    FINISH = "FINISH"

class AgentDecision(BaseModel):
    action: AgentAction
    reason: str = Field(min_length=1)