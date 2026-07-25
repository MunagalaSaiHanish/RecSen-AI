from app.agents.react_agent import run_react_agent


def main():
    incident = """
Payment API started returning HTTP 500 errors
immediately after version 2.4.1 was deployed.
"""

    service = "payment-api"

    conclusion = run_react_agent(
        incident=incident,
        service=service,
    )

    print("Incident:")
    print(incident)

    print("\nFinal investigation:")
    print(conclusion)




if __name__ == "__main__":
    main()