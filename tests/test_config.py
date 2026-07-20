from app.core.config import get_settings


settings = get_settings()

print(settings.app_name)
print(settings.app_env)
print(settings.debug)
print(settings.llm_model)
print(settings.max_agent_iterations)