from app.memory.repository import EpisodeRepository

class MemoryRetriever:
    def __init__(self):
        self.repository = EpisodeRepository()

    def retrieve(self, incident: str, limit: int = 3) -> list:
        episodes = self.repository.load_all()
        matches = []
        incident = incident.lower()
        for episode in episodes:
            if incident in episode.investigation.incident.lower():
                matches.append(episode)
        return matches[:limit]