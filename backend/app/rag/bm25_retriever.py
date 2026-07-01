from langchain_community.retrievers import BM25Retriever

from app.rag.loader import HospitalDocumentLoader
from app.rag.splitter import HospitalTextSplitter

from pathlib import Path


class BM25Search:

    def __init__(self):

        base_dir = Path(__file__).resolve().parents[2]

        documents_dir = base_dir.parent / "documents"

        loader = HospitalDocumentLoader(str(documents_dir))

        documents = loader.load_documents()

        splitter = HospitalTextSplitter()

        chunks = splitter.split_documents(documents)

        self.retriever = BM25Retriever.from_documents(chunks)

        self.retriever.k = 5

    def search(self, query: str):

        return self.retriever.invoke(query)