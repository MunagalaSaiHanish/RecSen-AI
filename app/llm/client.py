import json
import re

from openai import OpenAI
from pydantic import ValidationError

from app.core.config import settings
from app.schemas.agent import (
    AgentDecision,
    InvestigationPlan,
    ToolCall,
)
from app.tools.definitions import INVESTIGATION_TOOLS


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.llm_api_key,
)

def parse_json_response(content: str) -> dict:
    cleaned_content = content.strip()

    code_block_match = re.fullmatch(
        r"```(?:json)?\s*(.*?)\s*```",
        cleaned_content,
        re.DOTALL,
    )

    if code_block_match:
        cleaned_content = code_block_match.group(1).strip()

    try:
        return json.loads(cleaned_content)

    except json.JSONDecodeError as exc:
        raise ValueError(
            f"LLM returned invalid JSON: {content}"
        ) from exc


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
        data = parse_json_response(content)
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
        id=tool_call.id,
        name=tool_call.function.name,
        arguments=arguments,
    )


def create_agent_response(
    messages: list[dict],
):
    return client.chat.completions.create(
        model=settings.llm_model,
        messages=messages,
        tools=INVESTIGATION_TOOLS,
        tool_choice="auto",
        max_tokens=500,
    )


def generate_investigation_plan(
    incident: str,
    service: str,
    available_tools: list[dict],
    
) -> InvestigationPlan:
    tools_context = json.dumps(
    available_tools,
    indent=2,
)
    response = client.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {
    "role": "system",
    "content": (
        "You are the planning component of RECSEN, "
        "an incident investigation agent. "
        "Create a concise investigation plan. "
        "Break the investigation goal into ordered, "
        "purposeful steps. "
        "Only create steps that can be investigated "
        "using the available tools. "
        "Do not invent unavailable capabilities. "
        "Do not execute tools. "
        "Return only valid JSON matching the requested "
        "plan structure."
    ),
},
            {
    "role": "user",
    "content": (
        f"Incident:\n{incident}\n\n"
        f"Service: {service}\n\n"
        f"Available tools:\n{tools_context}\n\n"
        "Return JSON with this structure:\n"
        "{\n"
        '  "goal": "investigation goal",\n'
        '  "steps": [\n'
        "    {\n"
        '      "step_number": 1,\n'
        '      "description": "what to investigate",\n'
        '      "expected_outcome": "what this should reveal"\n'
        "    }\n"
        "  ]\n"
        "}"
    ),
},
        ],
        max_tokens=450,
    )

    content = response.choices[0].message.content

    if content is None:
        raise ValueError(
            "LLM returned an empty investigation plan."
        )

    try:
        data = parse_json_response(content)

        return InvestigationPlan.model_validate(data)

    except ValidationError as exc:
        raise ValueError(
            f"LLM returned an invalid investigation plan: {content}"
        ) from exc

def generate_revised_plan(
    incident: str,
    service: str,
    replanning_context: str,
    available_tools: list[dict],
) -> InvestigationPlan:
    tools_context = json.dumps(
        available_tools,
        indent=2,
    )

    response = client.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are the replanning component of RECSEN. "
                    "Review the current investigation state and "
                    "create a revised investigation plan. "
                    "Use the observations and failures from completed "
                    "steps when deciding what should happen next. "
                    "Do not repeat completed work unless there is a "
                    "clear reason to retry it. "
                    "Only create steps that can be performed using "
                    "the available tools. "
                    "Return only valid JSON matching the requested "
                    "plan structure."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Incident:\n{incident}\n\n"
                    f"Service: {service}\n\n"
                    f"Available tools:\n{tools_context}\n\n"
                    "Current investigation context:\n"
                    f"{replanning_context}\n\n"
                    "Return JSON with this structure:\n"
                    "{\n"
                    '  "goal": "investigation goal",\n'
                    '  "steps": [\n'
                    "    {\n"
                    '      "step_number": 1,\n'
                    '      "description": "what to investigate next",\n'
                    '      "expected_outcome": "what this should reveal"\n'
                    "    }\n"
                    "  ]\n"
                    "}"
                ),
            },
        ],
        max_tokens=450,
    )

    content = response.choices[0].message.content

    if content is None:
        raise ValueError(
            "LLM returned an empty revised plan."
        )

    try:
        data = parse_json_response(content)

        return InvestigationPlan.model_validate(data)

    except ValidationError as exc:
        raise ValueError(
            f"LLM returned an invalid revised plan: {content}"
        ) from exc