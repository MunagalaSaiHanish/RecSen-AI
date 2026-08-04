from app.rag.embedding_service import EmbeddingService


def test_embedding_dimension():
    service = EmbeddingService()
    assert service.dimension() == 384

def test_single_embedding():
    service = EmbeddingService()
    vector = service.embed_text(
        "Payment API failed"
    )
    assert len(vector) == 384

def test_batch_embeddings():
    service = EmbeddingService()
    vectors = service.embed_batch(
        [
            "Redis timeout",
            "Database failure",
        ]
    )
    assert len(vectors) == 2