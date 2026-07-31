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
        metadata=EpisodeMetadata(),
        investigation=InvestigationRecord(
            incident=incident,
            goal=execution_state.plan.goal,
            plan=execution_state.plan,
            completed_steps=execution_state.completed_steps,
            status=execution_state.status,
            replans=execution_state.replan_count,
        ),
        evidence=EvidenceSnapshot(
            working_memory=execution_state.working_memory,
        ),
        outcome=InvestigationOutcome(),
    )