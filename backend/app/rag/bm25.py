from rank_bm25 import BM25Okapi


class HospitalBM25:

    def __init__(self, documents):

        self.documents = documents

        self.tokenized_docs = [
            doc.page_content.lower().split()
            for doc in documents
        ]

        self.bm25 = BM25Okapi(self.tokenized_docs)

    def search(
        self,
        query: str,
        k: int = 5
    ):

        tokens = query.lower().split()

        scores = self.bm25.get_scores(tokens)

        ranked = sorted(
            zip(scores, self.documents),
            key=lambda x: x[0],
            reverse=True
        )

        return [
            doc
            for score, doc in ranked[:k]
        ]