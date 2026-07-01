class SQLIntentRouter:

    SQL_KEYWORDS = [
        "patient",
        "patients",
        "doctor",
        "doctors",
        "appointment",
        "appointments",
        "admission",
        "admissions",
        "bed",
        "beds",
        "icu",
        "billing",
        "bill",
        "revenue",
        "department",
        "available",
        "count",
        "today",
        "yesterday",
        "occupied",
        "inventory",
        "laboratory",
        "lab",
    ]

    def detect(self, question: str):

        question = question.lower()

        for keyword in self.SQL_KEYWORDS:
            if keyword in question:
                return "SQL"

        return "RAG"