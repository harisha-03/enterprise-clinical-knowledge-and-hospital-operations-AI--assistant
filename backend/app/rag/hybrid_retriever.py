from app.rag.query_expansion import QueryExpansion
from app.rag.vector_retriever import VectorRetriever
from app.rag.bm25_retriever import BM25Search


class HybridRetriever:

    def __init__(self):

        self.vector = VectorRetriever()

        self.bm25 = BM25Search()

        self.expander = QueryExpansion()

    def search(
        self,
        query: str,
        category: str | None = None,
        k: int = 5
    ):

        expanded_query = self.expander.expand(query)

        print(f"\nExpanded Query: {expanded_query}")

        vector_results = self.vector.search(
            query=expanded_query,
            category=category,
            k=k
        )

        bm25_results = self.bm25.search(expanded_query)

        combined = []

        seen = set()

        for doc in vector_results + bm25_results:

            key = (
                doc.metadata.get("source"),
                doc.metadata.get("page"),
                doc.page_content[:100]
            )

            if key not in seen:

                seen.add(key)

                combined.append(doc)

        return combined[:k]