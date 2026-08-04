from app.retrieval.memory_retriever import MemoryRetriever


class ContextBuilder:
    def __init__(self):
        self.retriever = MemoryRetriever()

    def build(self, incident: str) -> str:
        memories = self.retriever.retrieve(incident)
        if not memories:
            return ""
        lines = ["Relevant previous investigations:"]
        for episode in memories:
            lines.append(f"- {episode.investigation.incident}")
        return "\n".join(lines)