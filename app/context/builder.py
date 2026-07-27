import json

from app.schemas.agent import PlanExecutionState


def build_replanning_context(
    state: PlanExecutionState,
) -> str:
    completed_steps = []

    for execution in state.completed_steps:
        completed_steps.append(
            {
                "step_number": execution.step.step_number,
                "description": execution.step.description,
                "expected_outcome": (
                    execution.step.expected_outcome
                ),
                "tool_name": execution.tool_name,
                "success": execution.success,
                "observation": execution.observation,
            }
        )

    context = {
        "current_goal": state.plan.goal,
        "current_plan": [
            step.model_dump()
            for step in state.plan.steps
        ],
        "completed_steps": completed_steps,
    }

    return json.dumps(
        context,
        indent=2,
    )