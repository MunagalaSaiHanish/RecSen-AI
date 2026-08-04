from app.memory.consolidator import MemoryConsolidator

def test_memory_consolidation():
    consolidator = MemoryConsolidator()
    knowledge = [
        {
            "root_cause": "Redis",
            "resolution": "Restart",
        },
        {
            "root_cause": "Redis",
            "resolution": "Restart",
        },
    ]
    merged = consolidator.consolidate(knowledge)
    assert len(merged) == 1
    assert merged[0]["occurrences"] == 2