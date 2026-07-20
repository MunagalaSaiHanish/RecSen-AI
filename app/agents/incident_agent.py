from app.schemas.agent import AgentDecision


class IncidentAgent:
    def __init__(self, model):
        self.model = model

    def build_prompt(self, incident: str) -> str:
        return f"""
You are RECSEN AI, an incident investigation agent.

Your goal is to investigate technical incidents using evidence.

Incident:
{incident}

Available actions:
- QUERY_LOGS
- QUERY_METRICS
- CHECK_DEPLOYMENTS
- FINISH

Rules:
- Choose exactly one action.
- Choose only from the available actions.
- Do not claim a root cause without evidence.

Return a structured decision containing:
- action
- reason
"""

    def decide(self, incident: str) -> AgentDecision:
        prompt = self.build_prompt(incident)

        response = self.model.invoke(prompt)

        decision = AgentDecision.model_validate(response)

        return decision