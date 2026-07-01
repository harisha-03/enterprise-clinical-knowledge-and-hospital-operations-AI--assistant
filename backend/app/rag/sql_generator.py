from app.llm.factory import LLMFactory


SCHEMA = """
Database: PostgreSQL

Tables

patients
patient_id
first_name
last_name
gender
date_of_birth
blood_group
city
state

doctors
doctor_id
department_id
first_name
last_name
specialization
status

departments
department_id
department_name

appointments

admissions

beds
bed_id
department_id
bed_number
bed_type
room_number
floor_number
status

Possible Values

bed_type
ICU
General
Private
Semi-Private

status
Available
Occupied
Maintenance

billing

laboratory_results

medicine_inventory
"""


class SQLGenerator:

    def __init__(self):

        self.llm = LLMFactory.get_llm()

    def generate(self, question: str):

        prompt = f"""
You are an expert PostgreSQL developer.

Database Schema

{SCHEMA}

Rules

1. Generate ONLY SQL.
2. PostgreSQL syntax only.
3. ONLY SELECT statements.
4. Never use UPDATE, DELETE, INSERT, DROP, ALTER, CREATE.
5. Return ONLY executable SQL.
6. Never use markdown.
7. Always compare text using LOWER().

Example

Question:
How many ICU beds are available?

Answer:

SELECT COUNT(*) AS total
FROM beds
WHERE LOWER(bed_type)='icu'
AND LOWER(status)='available';

Question

{question}
"""

        sql = self.llm.generate(prompt)

        sql = sql.replace("```sql", "")
        sql = sql.replace("```", "")
        sql = sql.strip()

        return sql