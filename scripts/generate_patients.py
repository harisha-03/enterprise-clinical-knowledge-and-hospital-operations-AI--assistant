import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

insurance = pd.read_csv("datasets/insurance.csv")

insurance_ids = insurance["insurance_id"].tolist()

blood_groups = [
    "A+","A-","B+","B-",
    "AB+","AB-","O+","O-"
]

genders = [
    "Male",
    "Female"
]

cities = [
    "Bengaluru",
    "Mysuru",
    "Hubballi",
    "Mangaluru",
    "Ballari",
    "Belagavi",
    "Shivamogga",
    "Davanagere"
]

rows = []

for i in range(1,10001):

    rows.append([
        f"PAT{i:05}",
        fake.first_name(),
        fake.last_name(),
        random.choice(genders),
        fake.date_of_birth(minimum_age=1, maximum_age=90),
        random.choice(blood_groups),
        fake.msisdn()[:10],
        f"patient{i}@gmail.com",
        fake.street_address(),
        random.choice(cities),
        "Karnataka",
        "India",
        fake.name(),
        fake.msisdn()[:10],
        random.choice(insurance_ids)
    ])

columns = [
    "patient_id",
    "first_name",
    "last_name",
    "gender",
    "date_of_birth",
    "blood_group",
    "phone",
    "email",
    "address",
    "city",
    "state",
    "country",
    "emergency_contact_name",
    "emergency_contact_phone",
    "insurance_id"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "datasets/patients.csv",
    index=False
)

print(f"{len(df)} patients generated successfully!")