from app.tools.registry import TOOL_REGISTRY


INVESTIGATION_TOOLS = [
    tool.to_llm_definition()
    for tool in TOOL_REGISTRY.values()
]