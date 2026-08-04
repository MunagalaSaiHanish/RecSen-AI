from app.memory.procedural_memory import ProceduralMemory


def test_build_playbooks():
    memory = ProceduralMemory()
    playbooks = memory.build_playbooks()

    assert isinstance(playbooks, list)