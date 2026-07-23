from app.core.config import settings


def test_app_name():
    assert settings.app_name == "RECSEN AI"


def test_environment():
    assert settings.app_env == "development"