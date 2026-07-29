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

class ToolCall(BaseModel):
    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    arguments: dict[str, Any]


class PlanStep(BaseModel):
    step_number: int = Field(gt=0)
    description: str = Field(min_length=1)
    expected_outcome: str = Field(min_length=1)


class InvestigationPlan(BaseModel):
    goal: str = Field(min_length=1)
    steps: list[PlanStep] = Field(min_length=1)

class StepExecution(BaseModel):
    step: PlanStep
    tool_name: str | None = None
    observation: dict[str, Any] | None = None
    success: bool = False

class AgentStatus(str, Enum):
    PLANNING = "planning"
    EXECUTING = "executing"
    EVALUATING = "evaluating"
    REPLANNING = "replanning"
    COMPLETED = "completed"
    FAILED = "failed"


class PlanExecutionState(BaseModel):
    plan: InvestigationPlan
    completed_steps: list[StepExecution] = Field(
        default_factory=list
    )
    status: AgentStatus = AgentStatus.PLANNING
    current_step_index: int = 0
    replan_count: int = 0

