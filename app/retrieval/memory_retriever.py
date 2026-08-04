from app.memory.repository import EpisodeRepository


class MemoryRetriever:
    def __init__(self):
        self.repository = EpisodeRepository()

    def retrieve(
        self,
        incident: str,
        limit: int = 3,
    ) -> list[str]:
        episodes = self.repository.load_all()
        incident = incident.lower()
        memories = []
        for episode in episodes:
            if incident in episode.investigation.incident.lower():
                memories.append(
                    f"Incident: {episode.investigation.incident}\n"
                    f"Root Cause: {episode.outcome.root_cause}\n"
                    f"Resolution: {episode.outcome.resolution}"
                )
        return memories[:limit]