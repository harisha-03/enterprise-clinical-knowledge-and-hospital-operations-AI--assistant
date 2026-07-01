from pathlib import Path


class RAGSettings:

    # Project Paths
    BASE_DIR = Path(__file__).resolve().parents[2]

    DOCUMENTS_DIR = BASE_DIR.parent / "documents"

    VECTOR_DB_DIR = BASE_DIR / "chromadb"

    # Embedding Model
    EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

    # Chunking
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200

    # Retrieval
    TOP_K = 5

    # Query Expansion
    ENABLE_QUERY_EXPANSION = True

    # Hybrid Search
    ENABLE_BM25 = True

    # Reranker
    ENABLE_RERANKING = True