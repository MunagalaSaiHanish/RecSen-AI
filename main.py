from app.agents.incident_agent import decide_next_action
from app.tools.executor import execute_action

def main():
    incident = """
Payment API started returning HTTP 500 errors
immediately after version 2.4.1 was deployed.
"""
    service = "payment-api"
    decision = decide_next_action(incident)

    print("Incident:")
    print(incident)

    print("Agent decision:")
    print(f"Action: {decision.action.value}")
    print(f"Reason: {decision.reason}")

    observation = execute_action(
        action=decision.action,
        service=service,
    )
    print("\nObservation:")
    print(observation)
if __name__ == "__main__":
    main()