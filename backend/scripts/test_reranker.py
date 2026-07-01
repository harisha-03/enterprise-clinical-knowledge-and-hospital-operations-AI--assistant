from app.rag.hybrid_retriever import HybridRetriever
from app.rag.reranker import HospitalReranker


def main():

    print("=" * 70)
    print("Hybrid Search + Cross Encoder Reranker")
    print("=" * 70)

    retriever = HybridRetriever()

    reranker = HospitalReranker()

    while True:

        query = input("\nQuestion (exit to quit): ")

        if query.lower() == "exit":
            break

        category = input(
            "Category (Press Enter for All Documents): "
        ).strip()

        if category == "":
            category = None

        print("\nRunning Hybrid Search...")

        docs = retriever.search(
            query=query,
            category=category,
            k=10
        )

        print(f"Retrieved {len(docs)} candidate chunks")

        print("\nRunning Cross Encoder Reranker...")

        final_docs = reranker.rerank(
            query=query,
            documents=docs,
            top_k=5
        )

        print("\n" + "=" * 70)
        print("FINAL RANKED RESULTS")
        print("=" * 70)

        for i, doc in enumerate(final_docs, start=1):

            print(f"\nResult {i}")
            print("-" * 70)

            print("Document :", doc.metadata.get("document_name"))
            print("Category :", doc.metadata.get("category"))
            print("Page :", doc.metadata.get("page"))

            print("\n")

            print(doc.page_content[:500])


if __name__ == "__main__":
    main()