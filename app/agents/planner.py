from app.llm.client import generate_investigation_plan
from app.schemas.agent import InvestigationPlan
from app.tools.registry import TOOL_REGISTRY
from app.retrieval.memory_retriever import MemoryRetriever 


def create_investigation_plan(
    incident: str,
    service: str,
) -> InvestigationPlan:
    retriever = MemoryRetriever()

    memory_context = retriever.retrieve(
    incident=incident,
)
    available_tools = [
        {
            "name": tool.name,
            "description": tool.description,
        }
        for tool in TOOL_REGISTRY.values()
    ]

    retriever = MemoryRetriever()

    memory_context = retriever.retrieve(
            incident=incident,
)

    return generate_investigation_plan(
    incident=incident,
    service=service,
    available_tools=available_tools,
    memory_context=memory_context,
)