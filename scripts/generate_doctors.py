import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

departments = [
    ("DEP001", "Cardiology"),
    ("DEP002", "Neurology"),
    ("DEP003", "Orthopedics"),
    ("DEP004", "Emergency"),
    ("DEP005", "ICU"),
    ("DEP006", "Pediatrics"),
    ("DEP007", "Radiology"),
    ("DEP008", "Laboratory"),
    ("DEP009", "Oncology"),
    ("DEP010", "General Medicine")
]

qualifications = [
    "MBBS, MD",
    "MBBS, MS",
    "MBBS, DM",
    "MBBS, DNB"
]

rows = []

for i in range(1, 101):

    dept = random.choice(departments)

    rows.append([
        f"DOC{i:04}",
        dept[0],
        fake.first_name(),
        fake.last_name(),
        dept[1],
        random.choice(qualifications),
        random.randint(1, 35),
        fake.msisdn()[:10],
        f"doctor{i}@hospital.com",
        random.randint(300, 2000),
        "Active"
    ])

columns = [
    "doctor_id",
    "department_id",
    "first_name",
    "last_name",
    "specialization",
    "qualification",
    "experience_years",
    "phone",
    "email",
    "consultation_fee",
    "status"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "datasets/doctors.csv",
    index=False
)

print("doctors.csv generated successfully!")