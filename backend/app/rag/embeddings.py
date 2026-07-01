from langchain_huggingface import HuggingFaceEmbeddings

from app.core.settings import RAGSettings


class HospitalEmbeddings:

    def __init__(self):

        self.embedding = HuggingFaceEmbeddings(
            model_name=RAGSettings.EMBEDDING_MODEL
        )

    def get_embedding_model(self):

        return self.embedding