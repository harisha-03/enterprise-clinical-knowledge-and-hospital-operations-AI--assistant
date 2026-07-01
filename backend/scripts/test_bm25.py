from app.rag.bm25_retriever import BM25Search


def main():

    print("=" * 70)
    print("BM25 Keyword Search")
    print("=" * 70)

    bm25 = BM25Search()

    while True:

        query = input("\nQuestion (exit to quit): ")

        if query.lower() == "exit":
            break

        results = bm25.search(query)

        print("\n" + "=" * 70)
        print(f"Retrieved {len(results)} Results")
        print("=" * 70)

        for i, doc in enumerate(results, start=1):

            print(f"\nResult {i}")
            print("-" * 70)

            print("Document :", doc.metadata.get("document_name"))
            print("Category :", doc.metadata.get("category"))
            print("Page :", doc.metadata.get("page"))

            print("\nContent:\n")

            print(doc.page_content[:500])


if __name__ == "__main__":
    main()