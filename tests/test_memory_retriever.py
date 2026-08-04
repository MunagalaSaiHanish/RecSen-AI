from app.retrieval.memory_retriever import MemoryRetriever
def test_memory_retriever():

    retriever = MemoryRetriever()
    results = retriever.retrieve(
        "payment"
    )
    assert isinstance(
        results,
        list,
    )

    