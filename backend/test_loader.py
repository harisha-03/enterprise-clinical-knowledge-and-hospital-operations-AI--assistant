from pathlib import Path

from app.rag.loader import HospitalDocumentLoader
from app.rag.splitter import HospitalTextSplitter
from app.rag.vectorstore import HospitalVectorStore

BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENTS_DIR = BASE_DIR / "documents"

loader = HospitalDocumentLoader(str(DOCUMENTS_DIR))
documents = loader.load_documents()

print(f"Documents Loaded : {len(documents)}")

splitter = HospitalTextSplitter()

chunks = splitter.split_documents(documents)

print(f"Chunks Created : {len(chunks)}")

vectorstore = HospitalVectorStore().create_vectorstore(chunks)

print("\n✅ ChromaDB Created Successfully")
print(f"Total Chunks Stored : {vectorstore._collection.count()}")