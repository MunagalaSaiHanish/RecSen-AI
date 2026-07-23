def query_logs(service: str) -> dict:
    return {
        "service": service,
        "logs": [
            "ERROR Database connection timeout",
            "ERROR Connection pool exhausted",
            "ERROR Request failed with status 500",
        ],
    }


def query_metrics(service: str) -> dict:
    return {
        "service": service,
        "cpu_usage": 91,
        "memory_usage": 72,
        "error_rate": 17,
    }


def check_deployments(service: str) -> dict:
    return {
        "service": service,
        "version": "2.4.1",
        "status": "deployed",
        "minutes_ago": 15,
    }