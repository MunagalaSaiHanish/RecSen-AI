from app.agents.plan_executor import execute_plan


from app.agents.planner import create_investigation_plan        
from app.memory.episode_builder import build_episode
from app.memory.repository import EpisodeRepository


def main():
    incident = """
Payment API started returning HTTP 500 errors
immediately after version 2.4.1 was deployed.
"""

    service = "payment-api"

    print("Creating investigation plan...\n")

    plan = create_investigation_plan(
        incident=incident,
        service=service,
    )

    print("Investigation goal:")
    print(plan.goal)

    print("\nPlan:")

    for step in plan.steps:
        print(
            f"{step.step_number}. "
            f"{step.description}"
        )

    print("\nExecuting plan...\n")

    execution_state = execute_plan(
        plan=plan,
        incident=incident,
        service=service,
    )

    for execution in execution_state.completed_steps:
        print(
            f"Step {execution.step.step_number}: "
            f"{execution.step.description}"
        )

        print(
            f"Tool: {execution.tool_name}"
        )

        print(
            f"Success: {execution.success}"
        )

        print(
            f"Observation: {execution.observation}"
        )

        print("-" * 60)


        print(
    f"\nFinal agent status: "
    f"{execution_state.status.value}"
)

        print(
    f"Replans performed: "
    f"{execution_state.replan_count}"
)
        print("\nWorking memory:")

    for entry in execution_state.working_memory.entries:
        print(
        f"- Source: {entry.source}"
    )
        print(
        f"  Content: {entry.content}"
    )

    episode = build_episode(
    incident=incident,
    execution_state=execution_state,
    )

    repository = EpisodeRepository()

    repository.save(
    episode
)

print("\nEpisode saved successfully.")    


if __name__ == "__main__":
    main()