import random
import pandas as pd
from datetime import timedelta
from faker import Faker

fake = Faker("en_IN")

admissions = pd.read_csv("datasets/admissions.csv")

rows = []

for i, admission in admissions.iterrows():

    admission_date = pd.to_datetime(
        admission["admission_date"]
    ).date()

    discharge_date = admission_date + timedelta(
        days=random.randint(1, 15)
    )

    rows.append([
        f"DIS{i+1:05}",
        admission["admission_id"],
        admission["patient_id"],
        discharge_date,
        fake.time_object().strftime("%H:%M:%S"),
        fake.paragraph(nb_sentences=2),
        random.choice([
            "Recovered",
            "Referred",
            "Against Medical Advice",
            "Expired"
        ]),
        discharge_date + timedelta(
            days=random.randint(7, 30)
        )
    ])

columns = [
    "discharge_id",
    "admission_id",
    "patient_id",
    "discharge_date",
    "discharge_time",
    "discharge_summary",
    "discharge_status",
    "follow_up_date"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "datasets/discharges.csv",
    index=False
)

print(f"{len(df)} discharges generated successfully!")