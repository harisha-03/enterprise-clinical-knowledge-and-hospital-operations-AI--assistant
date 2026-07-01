import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

department_ids = [
    "DEP001",
    "DEP002",
    "DEP003",
    "DEP004",
    "DEP005",
    "DEP006",
    "DEP007",
    "DEP008",
    "DEP009",
    "DEP010"
]

qualifications = [
    "GNM",
    "B.Sc Nursing",
    "M.Sc Nursing",
    "Post Basic B.Sc Nursing"
]

shifts = [
    "Morning",
    "Afternoon",
    "Night"
]

rows = []

for i in range(1, 251):

    rows.append([
        f"NUR{i:04}",
        random.choice(department_ids),
        fake.first_name(),
        fake.last_name(),
        random.choice(qualifications),
        random.randint(1, 25),
        random.choice(shifts),
        fake.msisdn()[:10],
        f"nurse{i}@hospital.com",
        "Active"
    ])

columns = [
    "nurse_id",
    "department_id",
    "first_name",
    "last_name",
    "qualification",
    "experience_years",
    "shift",
    "phone",
    "email",
    "status"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "datasets/nurses.csv",
    index=False
)

print("nurses.csv generated successfully!")