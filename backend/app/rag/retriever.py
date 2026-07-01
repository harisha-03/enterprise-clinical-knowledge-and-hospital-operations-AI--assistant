from app.rag.hybrid_retriever import HybridRetriever


class HospitalRetriever:

    def __init__(self):

        self.hybrid = HybridRetriever()

    def search(
        self,
        query: str,
        category: str | None = None,
        k: int = 5
    ):

        return self.hybrid.search(
            query=query,
            category=category,
            k=k
        )