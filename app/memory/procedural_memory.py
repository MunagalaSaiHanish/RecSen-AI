from app.memory.repository import EpisodeRepository

class ProceduralMemory:
    def __init__(self):
        self.repository = EpisodeRepository()

    def build_playbooks(self) -> list[dict]:
        episodes = self.repository.load_all()
        playbooks = []
        for episode in episodes:
            procedure = {
                "goal": episode.investigation.goal,
                "steps": [
                    step.description
                    for step in episode.investigation.plan.steps
                ],
            }
            playbooks.append(procedure)

        return playbooks