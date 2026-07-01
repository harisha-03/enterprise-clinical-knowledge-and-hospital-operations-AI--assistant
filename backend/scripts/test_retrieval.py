from app.rag.retriever import HospitalRetriever


def main():

    retriever = HospitalRetriever()

    print("=" * 70)
    print("Enterprise Hospital RAG Search")
    print("=" * 70)

    while True:

        query = input("\nQuestion (exit to quit): ")

        if query.lower() == "exit":
            break

        category = input(
            "Category (Press Enter for All Documents): "
        )

        category = category.strip()

        if category == "":
            category = None

        results = retriever.search(
            query=query,
            category=category
        )

        print("\n" + "=" * 70)

        print(f"Retrieved {len(results)} Results")

        print("=" * 70)

        for i, doc in enumerate(results, start=1):

            print(f"\nResult {i}")

            print("-" * 70)

            print("Document :", doc.metadata.get("document_name"))

            print("Category :", doc.metadata.get("category"))

            print("Department :", doc.metadata.get("department"))

            print("Source :", doc.metadata.get("source_type"))

            print("Page :", doc.metadata.get("page"))

            print()

            print(doc.page_content[:500])


if __name__ == "__main__":
    main()