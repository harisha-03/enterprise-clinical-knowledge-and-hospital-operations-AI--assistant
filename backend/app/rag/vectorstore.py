from langchain_chroma import Chroma

from app.core.settings import RAGSettings
from app.rag.embeddings import HospitalEmbeddings


class HospitalVectorStore:

    def __init__(self):

        self.embedding_model = HospitalEmbeddings().get_embedding_model()

        self.persist_directory = RAGSettings.VECTOR_DB_DIR

    def create_vectorstore(self, chunks):

        return Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=str(self.persist_directory)
        )

    def load_vectorstore(self):

        return Chroma(
            persist_directory=str(self.persist_directory),
            embedding_function=self.embedding_model
        )