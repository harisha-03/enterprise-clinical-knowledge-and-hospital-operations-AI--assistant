from pathlib import Path
from typing import List

from langchain_core.documents import Document

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    Docx2txtLoader,
    UnstructuredExcelLoader,
)

from app.rag.metadata import MetadataExtractor


class HospitalDocumentLoader:

    def __init__(self, documents_path: str):

        self.documents_path = Path(documents_path)

        self.metadata = MetadataExtractor()

        self.loaders = {
            ".pdf": PyPDFLoader,
            ".txt": TextLoader,
            ".csv": CSVLoader,
            ".docx": Docx2txtLoader,
            ".xlsx": UnstructuredExcelLoader,
        }

    def load_documents(self) -> List[Document]:

        documents = []

        for file in self.documents_path.rglob("*"):

            if not file.is_file():
                continue

            extension = file.suffix.lower()

            if extension not in self.loaders:
                continue

            try:

                loader = self.loaders[extension](str(file))

                docs = loader.load()

                for doc in docs:

                    doc = self.metadata.enrich(doc)

                    documents.append(doc)

                print(f"✅ Loaded : {file.name}")

            except Exception as e:

                print(f"❌ Failed : {file.name}")

                print(e)

        return documents