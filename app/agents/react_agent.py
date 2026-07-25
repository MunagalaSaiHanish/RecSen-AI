import json

from app.llm.client import create_agent_response
from app.schemas.agent import ToolCall
from app.tools.executor import execute_tool_call


MAX_STEPS = 5


def run_react_agent(
    incident: str,
    service: str,
) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are RECSEN, an incident investigation agent. "
                "Investigate incidents using available tools. "
                "Base conclusions on evidence returned by tools. "
                "Do not repeat tools unnecessarily. "
                "When enough evidence has been collected, return "
                "a concise final investigation conclusion."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Incident:\n{incident}\n\n"
                f"Service: {service}"
            ),
        },
    ]

    for _ in range(MAX_STEPS):
        response = create_agent_response(messages)

        assistant_message = response.choices[0].message

        messages.append(
            assistant_message.model_dump(
                exclude_none=True
            )
        )

        if not assistant_message.tool_calls:
            return (
                assistant_message.content
                or "Investigation completed without a conclusion."
            )

        for raw_tool_call in assistant_message.tool_calls:
            arguments = json.loads(
                raw_tool_call.function.arguments
            )

            tool_call = ToolCall(
                id=raw_tool_call.id,
                name=raw_tool_call.function.name,
                arguments=arguments,
            )

            observation = execute_tool_call(tool_call)

            print(f"\nTool call: {tool_call.name}")
            print(f"Arguments: {tool_call.arguments}")
            print(f"Observation: {observation.model_dump()}")

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": observation.model_dump_json(),
                }
            )

    return (
        "Investigation stopped because the maximum "
        "step limit was reached."
    )