import os

from app.llm.gemini import GeminiLLM
from app.llm.ollama import OllamaLLM


class LLMFactory:

    @staticmethod
    def get_llm():

        provider = os.getenv(
            "LLM_PROVIDER",
            "gemini"
        ).lower()

        if provider == "ollama":
            return OllamaLLM()

        return GeminiLLM()