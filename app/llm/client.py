import json
from openai import OpenAI
from pydantic import ValidationError
from app.core.config import settings
from app.schemas.agent import AgentDecision
from app.schemas.agent import ToolCall
from app.tools.definitions import INVESTIGATION_TOOLS

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.llm_api_key,
)
def generate_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=200,
    )
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("LLM returned an empty response.")
    return content

def generate_agent_decision(prompt: str) -> AgentDecision:
    response = client.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=300,
    )
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("LLM returned an empty response.")
    try:
        data = json.loads(content)
        return AgentDecision.model_validate(data)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"LLM returned invalid JSON: {content}"
        ) from exc
    except ValidationError as exc:
        raise ValueError(
            f"LLM returned invalid AgentDecision: {content}"
        ) from exc

def generate_tool_call(
    messages: list[dict],
) -> ToolCall | None:
    response = client.chat.completions.create(
        model=settings.llm_model,
        messages=messages,
        tools=INVESTIGATION_TOOLS,
        tool_choice="auto",
        max_tokens=300,
    )

    message = response.choices[0].message

    if not message.tool_calls:
        return None

    tool_call = message.tool_calls[0]

    arguments = json.loads(
        tool_call.function.arguments
    )

    return ToolCall(
        name=tool_call.function.name,
        arguments=arguments,
    )