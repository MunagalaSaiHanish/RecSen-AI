from pydantic import ValidationError

from app.schemas.agent import ToolCall
from app.schemas.tools import ToolResult
from app.tools.registry import TOOL_REGISTRY


def execute_tool_call(
    tool_call: ToolCall,
) -> ToolResult:
    tool = TOOL_REGISTRY.get(tool_call.name)

    if tool is None:
        return ToolResult(
            success=False,
            tool_name=tool_call.name,
            error=f"Unknown tool: {tool_call.name}",
        )

    try:
        validated_input = tool.input_model.model_validate(
            tool_call.arguments
        )

        result = tool.function(
            **validated_input.model_dump()
        )

        return ToolResult(
            success=True,
            tool_name=tool.name,
            data=result,
        )

    except ValidationError as exc:
        return ToolResult(
            success=False,
            tool_name=tool.name,
            error=f"Invalid tool arguments: {exc}",
        )

    except Exception as exc:
        return ToolResult(
            success=False,
            tool_name=tool.name,
            error=f"Tool execution failed: {exc}",
        )