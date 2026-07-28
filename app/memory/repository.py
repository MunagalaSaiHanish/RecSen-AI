from app.memory.storage import (
    read_json,
    write_json,
)
from app.schemas.agent import (
    Episode,
)
"""Ep repo"""
class EpisodeRepository:
    def load_all(
        self,
    ) -> list[Episode]:
        raw = read_json()
        return [
            Episode(
                **episode
            )
            for episode in raw
        ]
    def save(
        self,
        episode: Episode,
    ) -> None:
        episodes = self.load_all()
        episodes.append(
            episode
        )
        serialized = [
            item.model_dump(
                mode="json"
            )
            for item in episodes
        ]
        write_json(
            serialized
        )