from app.schemas.agent import ToolCall
from app.tools.executor import execute_tool_call


def test_execute_registered_tool():
    tool_call = ToolCall(
        id="test-call-1",
        name="query_logs",
        arguments={
            "service": "payment-api",
        },
    )

    result = execute_tool_call(tool_call)

    assert result.success is True
    assert result.tool_name == "query_logs"
    assert result.data is not None
    assert result.data["service"] == "payment-api"


def test_reject_unknown_tool():
    tool_call = ToolCall(
        id="test-call-2",
        name="delete_database",
        arguments={},
    )

    result = execute_tool_call(tool_call)

    assert result.success is False
    assert result.error is not None
    assert "Unknown tool" in result.error


def test_reject_invalid_arguments():
    tool_call = ToolCall(
        id="test-call-3",
        name="query_logs",
        arguments={
            "service": "",
        },
    )

    result = execute_tool_call(tool_call)

    assert result.success is False
    assert result.error is not None
    assert "Invalid tool arguments" in result.error