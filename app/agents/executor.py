import json
from app.llm.client import create_agent_response
from app.schemas.agent import (
    PlanStep,
    StepExecution,
    ToolCall,
)
from app.tools.executor import execute_tool_call

def execute_plan_step(
    step: PlanStep,
    service: str,
) -> StepExecution:
    messages = [
        {
            "role": "system",
            "content": (
                "You are the execution component of RECSEN. "
                "Your job is to execute one investigation plan "
                "step using the available tools. "
                "Choose the single most appropriate tool for "
                "the requested step. Do not create a new plan."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Service: {service}\n\n"
                f"Plan step: {step.description}\n\n"
                f"Expected outcome: {step.expected_outcome}"
            ),
        },
    ]

    response = create_agent_response(messages)

    message = response.choices[0].message

    if not message.tool_calls:
        return StepExecution(
            step=step,
            success=False,
        )

    llm_tool_call = message.tool_calls[0]

    try:
        arguments = json.loads(
            llm_tool_call.function.arguments
        )

    except json.JSONDecodeError:
        return StepExecution(
            step=step,
            tool_name=llm_tool_call.function.name,
            success=False,
        )

    tool_call = ToolCall(
        id=llm_tool_call.id,
        name=llm_tool_call.function.name,
        arguments=arguments,
    )

    result = execute_tool_call(
        tool_call
    )

    return StepExecution(
        step=step,
        tool_name=result.tool_name,
        observation=result.model_dump(),
        success=result.success,
    )