from app.memory.repository import EpisodeRepository

class SemanticMemory:
    def __init__(self):
        self.repository = EpisodeRepository()

    def build_knowledge(self) -> list[dict]:
        episodes = self.repository.load_all()
        knowledge = []
        for episode in episodes:
            fact = {
                "incident": episode.investigation.incident,
                "root_cause": episode.outcome.root_cause,
                "resolution": episode.outcome.resolution,
            }
            knowledge.append(fact)
        return knowledge