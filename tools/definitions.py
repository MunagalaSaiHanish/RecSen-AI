INVESTIGATION_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "query_logs",
            "description": (
                "Retrieve recent application error logs for a service. "
                "Use this when investigating exceptions, failures, "
                "timeouts, or HTTP 5xx errors."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "service": {
                        "type": "string",
                        "description": "Name of the service to inspect.",
                    }
                },
                "required": ["service"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_metrics",
            "description": (
                "Retrieve runtime metrics for a service, including "
                "CPU usage, memory usage, and error rate."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "service": {
                        "type": "string",
                        "description": "Name of the service to inspect.",
                    }
                },
                "required": ["service"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "check_deployments",
            "description": (
                "Retrieve recent deployment information for a service. "
                "Use this when investigating whether a deployment "
                "may be related to an incident."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "service": {
                        "type": "string",
                        "description": "Name of the service to inspect.",
                    }
                },
                "required": ["service"],
                "additionalProperties": False,
            },
        },
    },
]