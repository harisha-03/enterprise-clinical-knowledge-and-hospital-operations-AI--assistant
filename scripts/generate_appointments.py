import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

patients = pd.read_csv("datasets/patients.csv")
doctors = pd.read_csv("datasets/doctors.csv")

patient_ids = patients["patient_id"].tolist()

doctor_ids = doctors["doctor_id"].tolist()

doctor_department = dict(
    zip(
        doctors["doctor_id"],
        doctors["department_id"]
    )
)

appointment_types = [
    "Consultation",
    "Follow-up",
    "Emergency",
    "Routine Checkup"
]

status = [
    "Scheduled",
    "Completed",
    "Cancelled"
]

rows = []

for i in range(1,50001):

    doctor = random.choice(doctor_ids)

    rows.append([
        f"APT{i:06}",
        random.choice(patient_ids),
        doctor,
        doctor_department[doctor],
        fake.date_between(start_date="-2y", end_date="+6m"),
        fake.time_object().strftime("%H:%M:%S"),
        random.choice(appointment_types),
        fake.sentence(nb_words=6),
        random.choice(status)
    ])

columns = [
    "appointment_id",
    "patient_id",
    "doctor_id",
    "department_id",
    "appointment_date",
    "appointment_time",
    "appointment_type",
    "reason_for_visit",
    "status"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "datasets/appointments.csv",
    index=False
)

print(f"{len(df)} appointments generated successfully!")