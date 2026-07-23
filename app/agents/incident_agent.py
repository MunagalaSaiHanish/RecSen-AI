from app.llm.client import generate_agent_decision
from app.schemas.agent import AgentDecision


def decide_next_action(incident: str) -> AgentDecision:
    prompt = f"""
You are an incident investigation agent.

Your goal is to investigate production incidents and decide
the most useful next action.

Incident:
{incident}

Choose exactly one action:

CHECK_LOGS
CHECK_METRICS
CHECK_DEPLOYMENTS
FINISH

Return ONLY valid JSON in exactly this structure:

{{
    "action": "CHECK_LOGS",
    "reason": "Brief explanation of why this is the best next action."
}}

Do not include markdown.
Do not include code fences.
Do not include text before or after the JSON.
"""

    return generate_agent_decision(prompt)