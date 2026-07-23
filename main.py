from app.agents.runner import run_investigation


def main():
    incident = """
The website is unexpectedly broken down and payments were not initializing caused payment failures
"""

    service = "payment-api"

    state = run_investigation(
        incident=incident,
        service=service,
    )

    print("Incident:")
    print(state.incident)

    print("\nInvestigation:")

    for index, step in enumerate(state.steps, start=1):
        print(f"\nStep {index}")
        print(f"Action: {step.action.value}")
        print(f"Reason: {step.reason}")
        print(f"Observation: {step.observation}")

    print("\nFinished:")
    print(state.finished)


if __name__ == "__main__":
    main()