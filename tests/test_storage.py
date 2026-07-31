from app.memory.storage import (
    load_episodes,
)


def test_load_returns_list():
    episodes = load_episodes()

    assert isinstance(
        episodes,
        list,
    )