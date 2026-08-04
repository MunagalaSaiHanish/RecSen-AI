from app.memory.semantic_memory import SemanticMemory

def test_semantic_memory_creation():
    memory = SemanticMemory()
    knowledge = memory.build_knowledge()

    assert isinstance(knowledge, list)