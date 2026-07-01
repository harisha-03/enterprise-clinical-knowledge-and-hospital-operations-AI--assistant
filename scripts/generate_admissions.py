import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

patients = pd.read_csv("datasets/patients.csv")
doctors = pd.read_csv("datasets/doctors.csv")
beds = pd.read_csv("datasets/beds.csv")

patient_ids = patients["patient_id"].tolist()
doctor_ids = doctors["doctor_id"].tolist()
bed_ids = beds["bed_id"].tolist()

admission_types = [
    "Emergency",
    "Elective",
    "Observation",
    "Day Care"
]

status = [
    "Admitted",
    "Discharged",
    "Transferred"
]

rows = []

for i in range(1,8001):

    admission_date = fake.date_between(start_date="-2y", end_date="today")

    rows.append([
        f"ADM{i:05}",
        random.choice(patient_ids),
        random.choice(doctor_ids),
        random.choice(bed_ids),
        admission_date,
        fake.time_object().strftime("%H:%M:%S"),
        fake.sentence(nb_words=6),
        random.choice(admission_types),
        fake.date_between(start_date=admission_date, end_date="+15d"),
        random.choice(status)
    ])

columns = [
    "admission_id",
    "patient_id",
    "doctor_id",
    "bed_id",
    "admission_date",
    "admission_time",
    "admission_reason",
    "admission_type",
    "expected_discharge_date",
    "status"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "datasets/admissions.csv",
    index=False
)

print(f"{len(df)} admissions generated successfully!")