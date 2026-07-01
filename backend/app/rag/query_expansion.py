class QueryExpansion:

    MEDICAL_SYNONYMS = {

        "bp": [
            "blood pressure",
            "hypertension"
        ],

        "htn": [
            "hypertension",
            "high blood pressure"
        ],

        "dm": [
            "diabetes",
            "diabetes mellitus",
            "blood sugar"
        ],

        "tb": [
            "tuberculosis"
        ],

        "mi": [
            "myocardial infarction",
            "heart attack"
        ],

        "cvvh": [
            "continuous veno venous haemodialysis"
        ],

        "dengue": [
            "dengue fever",
            "dengue virus",
            "dengue treatment"
        ],

        "copd": [
            "chronic obstructive pulmonary disease"
        ],

        "ckd": [
            "chronic kidney disease"
        ]

    }

    def expand(self, query: str) -> str:

        expanded = [query]

        words = query.lower().split()

        for word in words:

            if word in self.MEDICAL_SYNONYMS:

                expanded.extend(
                    self.MEDICAL_SYNONYMS[word]
                )

        return " ".join(expanded)