from app.llm.client import generate_tool_call
from app.tools.executor import execute_tool_call


def main():
    messages = [
        {
            "role": "user",
            "content": (
                "The payment-api started returning HTTP 500 "
                "errors. Investigate the most useful evidence first. "
                "Use an available tool."
            ),
        }
    ]

    tool_call = generate_tool_call(messages)

    if tool_call is None:
        print("Model did not request a tool.")
        return

    print("Tool requested:")
    print(tool_call.name)

    print("\nArguments:")
    print(tool_call.arguments)

    result = execute_tool_call(tool_call)

    print("\nTool result:")
    print(result)


if __name__ == "__main__":
    main()