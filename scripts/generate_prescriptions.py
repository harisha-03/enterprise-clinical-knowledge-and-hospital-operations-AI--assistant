import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

patients = pd.read_csv("datasets/patients.csv")
doctors = pd.read_csv("datasets/doctors.csv")
medicines = pd.read_csv("datasets/pharmacy_inventory.csv")

patient_ids = patients["patient_id"].tolist()
doctor_ids = doctors["doctor_id"].tolist()
medicine_ids = medicines["medicine_id"].tolist()

dosages = [
    "250 mg",
    "500 mg",
    "650 mg",
    "5 ml",
    "10 ml"
]

frequencies = [
    "Once Daily",
    "Twice Daily",
    "Three Times Daily",
    "Every 8 Hours",
    "SOS"
]

rows = []

for i in range(1, 40001):

    rows.append([
        f"PRE{i:06}",
        random.choice(patient_ids),
        random.choice(doctor_ids),
        random.choice(medicine_ids),
        random.choice(dosages),
        random.choice(frequencies),
        random.randint(3,30),
        random.randint(1,20),
        fake.sentence(nb_words=6),
        fake.date_between(start_date="-2y", end_date="today")
    ])

columns = [
    "prescription_id",
    "patient_id",
    "doctor_id",
    "medicine_id",
    "dosage",
    "frequency",
    "duration_days",
    "quantity",
    "instructions",
    "prescription_date"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "datasets/prescriptions.csv",
    index=False
)

print(f"{len(df)} prescriptions generated successfully!")