import re


class IntentRouter:

    def detect_intent(self, query: str):

        query = query.lower()

        # Database Queries
        if re.search(r"\b(patient|doctor|appointment|admission|billing|laboratory|lab)\b", query):
            return "DATABASE"

        # Report Queries
        if re.search(r"\b(report|summary|dashboard|analytics|statistics)\b", query):
            return "REPORT"

        # Greeting
        if re.search(r"\b(hi|hello|hey)\b", query):
            return "GENERAL"

        # Default
        return "RAG"