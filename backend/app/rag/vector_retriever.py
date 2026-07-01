from app.core.settings import RAGSettings
from app.rag.vectorstore import HospitalVectorStore


class VectorRetriever:

    def __init__(self):

        self.vectorstore = HospitalVectorStore().load_vectorstore()

    def search(
        self,
        query: str,
        category: str | None = None,
        k: int = RAGSettings.TOP_K
    ):

        if category:

            retriever = self.vectorstore.as_retriever(
                search_kwargs={
                    "k": k,
                    "filter": {
                        "category": category
                    }
                }
            )

        else:

            retriever = self.vectorstore.as_retriever(
                search_kwargs={
                    "k": k
                }
            )

        return retriever.invoke(query)