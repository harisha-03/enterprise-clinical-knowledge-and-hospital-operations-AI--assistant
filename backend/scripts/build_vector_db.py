from pathlib import Path

from app.rag.loader import HospitalDocumentLoader
from app.rag.splitter import HospitalTextSplitter
from app.rag.vectorstore import HospitalVectorStore


def main():

    print("=" * 70)
    print("Enterprise AI Hospital Knowledge Base Builder")
    print("=" * 70)

    base_dir = Path(__file__).resolve().parent.parent

    documents_dir = base_dir.parent / "documents"

    print("\n[1/4] Loading Documents...")

    loader = HospitalDocumentLoader(str(documents_dir))

    documents = loader.load_documents()

    print(f"Loaded {len(documents)} documents")

    print("\n[2/4] Splitting Documents...")

    splitter = HospitalTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("\n[3/4] Creating ChromaDB...")

    vectorstore = HospitalVectorStore().create_vectorstore(chunks)

    print("\n[4/4] Completed")

    print("=" * 70)
    print("Knowledge Base Built Successfully")
    print(f"Documents : {len(documents)}")
    print(f"Chunks    : {vectorstore._collection.count()}")
    print("=" * 70)


if __name__ == "__main__":
    main()