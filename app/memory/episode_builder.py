import uuid

from app.schemas.agent import (
    Episode,
    EpisodeMetadata,
    EvidenceSnapshot,
    InvestigationOutcome,
    InvestigationRecord,
    PlanExecutionState,
)


def build_episode(
    incident: str,
    execution_state: PlanExecutionState,
) -> Episode:

    return Episode(
        metadata=EpisodeMetadata(
            episode_id=str(
                uuid.uuid4()
            )
        ),
        investigation=InvestigationRecord(
            incident=incident,
            goal=execution_state.plan.goal,
            status=execution_state.status,
            replans=execution_state.replan_count,
            plan=execution_state.plan,
            completed_steps=execution_state.completed_steps,
        ),
        evidence=EvidenceSnapshot(
            working_memory=execution_state.working_memory,
        ),
        outcome=InvestigationOutcome(),
    )