from typing import Any

from app.schemas.agent import ToolCall
from app.tools.registry import TOOL_REGISTRY


def execute_tool_call(
    tool_call: ToolCall,
) -> dict[str, Any]:
    tool = TOOL_REGISTRY.get(tool_call.name)

    if tool is None:
        raise ValueError(
            f"Unknown tool: {tool_call.name}"
        )

    result = tool(**tool_call.arguments)

    return result