from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.settings import RAGSettings


class HospitalTextSplitter:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=RAGSettings.CHUNK_SIZE,
            chunk_overlap=RAGSettings.CHUNK_OVERLAP
        )

    def split_documents(self, documents):

        return self.splitter.split_documents(documents)