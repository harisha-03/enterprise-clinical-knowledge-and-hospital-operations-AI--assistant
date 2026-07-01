from app.rag.loader import HospitalDocumentLoader
from app.rag.bm25 import HospitalBM25
from app.rag.retriever import HospitalRetriever

from pathlib import Path


class HybridSearch:

    def __init__(self):

        base_dir = Path(__file__).resolve().parents[2]

        documents_dir = base_dir.parent / "documents"

        loader = HospitalDocumentLoader(str(documents_dir))

        self.documents = loader.load_documents()

        self.bm25 = HospitalBM25(self.documents)

        self.vector = HospitalRetriever()

    def search(
        self,
        query: str,
        k: int = 5
    ):

        vector_results = self.vector.search(
            query=query,
            k=k
        )

        bm25_results = self.bm25.search(
            query=query,
            k=k
        )

        merged = []

        seen = set()

        for doc in vector_results + bm25_results:

            key = (
                doc.metadata.get("source"),
                doc.metadata.get("page"),
                doc.page_content[:100]
            )

            if key not in seen:

                seen.add(key)

                merged.append(doc)

        return merged[:k]