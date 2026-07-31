from app.schemas.agent import (
    IncidentEpisode,
    PlanExecutionState,
)


def create_episode(
    incident: str,
    execution_state: PlanExecutionState,
) -> IncidentEpisode:
    return IncidentEpisode(
        incident=incident,
        completed_steps=execution_state.completed_steps,
    )