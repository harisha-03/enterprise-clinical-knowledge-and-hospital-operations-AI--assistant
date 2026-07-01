from pathlib import Path


class MetadataExtractor:

    CATEGORY_MAPPING = {

        "clinical_guidelines": {
            "category": "Clinical Guideline",
            "source_type": "WHO",
            "department": "Clinical"
        },

        "hospital_sops": {
            "category": "Hospital SOP",
            "source_type": "Hospital",
            "department": "Operations"
        },

        "hospital_policies": {
            "category": "Hospital Policy",
            "source_type": "Hospital",
            "department": "Administration"
        },

        "emergency_protocols": {
            "category": "Emergency Protocol",
            "source_type": "Hospital",
            "department": "Emergency"
        },

        "laboratory_manuals": {
            "category": "Laboratory Manual",
            "source_type": "Hospital",
            "department": "Laboratory"
        },

        "medical_books": {
            "category": "Medical Reference",
            "source_type": "Book",
            "department": "Education"
        },

        "nursing_protocols": {
            "category": "Nursing Protocol",
            "source_type": "Hospital",
            "department": "Nursing"
        }

    }

    def enrich(self, document):

        source = Path(document.metadata["source"])

        folder = source.parent.name

        info = self.CATEGORY_MAPPING.get(folder, {})

        document.metadata.update({

            "document_name": source.stem,

            "file_name": source.name,

            **info

        })

        return document