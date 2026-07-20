from pydantic import ValidationError

from app.schemas.agent import AgentDecision


valid_decision = AgentDecision(
    action="QUERY_METRICS",
    reason="Metrics can reveal resource bottlenecks.",
)

print(valid_decision)
print(valid_decision.action)
print(valid_decision.reason)


try:
    invalid_decision = AgentDecision(
        action="DELETE_DATABASE",
        reason="Try deleting the database.",
    )
except ValidationError as error:
    print(error)