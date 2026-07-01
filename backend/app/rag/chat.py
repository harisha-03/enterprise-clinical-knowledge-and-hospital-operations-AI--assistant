import os

from dotenv import load_dotenv

from app.llm.factory import LLMFactory
from app.rag.memory import ConversationMemory
from app.rag.intent import IntentRouter
from app.rag.sql_intent import SQLIntentRouter
from app.rag.sql_generator import SQLGenerator
from app.rag.sql_executor import SQLExecutor
from app.rag.retriever import HospitalRetriever
from app.rag.reranker import HospitalReranker

load_dotenv()


class HospitalAIChat:

    def __init__(self):

        self.llm = LLMFactory.get_llm()

        self.memory = ConversationMemory()

        self.intent_router = IntentRouter()

        self.sql_router = SQLIntentRouter()

        self.sql_generator = SQLGenerator()

        self.sql_executor = SQLExecutor()

        self.retriever = HospitalRetriever()

        self.reranker = HospitalReranker()

    def ask(self, question: str):

        # ==================================================
        # SQL MODULE
        # ==================================================

        sql_intent = self.sql_router.detect(question)

        if sql_intent == "SQL":

            try:

                sql = self.sql_generator.generate(question)

                print("\n================ GENERATED SQL ================\n")
                print(sql)
                print("\n===============================================\n")

                rows = self.sql_executor.execute(sql)

                prompt = f"""
You are an Enterprise Hospital AI Assistant.

Question:

{question}

Database Result:

{rows}

Answer naturally.

Do not mention SQL.

If no records are found, clearly say so.
"""

                answer = self.llm.generate(prompt)

                return {
                    "intent": "SQL",
                    "answer": answer,
                    "sources": []
                }

            except Exception as e:

                return {
                    "intent": "SQL",
                    "answer": str(e),
                    "sources": []
                }

        # ==================================================
        # RAG MODULE
        # ==================================================

        intent = self.intent_router.detect_intent(question)

        if intent != "RAG":

            return {
                "intent": intent,
                "answer": f"This request belongs to the {intent} module."
            }

        docs = self.retriever.search(
            query=question,
            k=10
        )

        docs = self.reranker.rerank(
            query=question,
            documents=docs,
            top_k=5
        )

        context = ""

        for i, doc in enumerate(docs, start=1):

            context += f"""
Source {i}

Document: {doc.metadata.get("document_name")}
Page: {doc.metadata.get("page")}

{doc.page_content}

----------------------------------------------------
"""

        prompt = f"""
You are an Enterprise Clinical AI Assistant.

Answer ONLY using the provided context.

Rules:

- Do not hallucinate.
- If the answer is not found, say so.
- Be concise.
- Mention document names where appropriate.

Context:

{context}

Question:

{question}
"""

        answer = self.llm.generate(prompt)

        self.memory.add_message("user", question)
        self.memory.add_message("assistant", answer)

        return {
            "intent": "RAG",
            "answer": answer,
            "sources": [
                {
                    "document": doc.metadata.get("document_name"),
                    "page": doc.metadata.get("page")
                }
                for doc in docs
            ]
        }