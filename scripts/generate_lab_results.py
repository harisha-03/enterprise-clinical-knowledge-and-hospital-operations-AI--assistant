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

tests = [
    "Complete Blood Count",
    "Blood Sugar",
    "Liver Function Test",
    "Kidney Function Test",
    "Lipid Profile",
    "Thyroid Profile",
    "ECG",
    "X-Ray Chest",
    "MRI Brain",
    "CT Scan",
    "Urine Analysis",
    "COVID-19 Test"
]

sample_types = [
    "Blood",
    "Urine",
    "Saliva",
    "Imaging"
]

statuses = [
    "Completed",
    "Pending"
]

rows = []

for i in range(1, 30001):

    doctor = random.choice(doctor_ids)

    test_date = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    report_date = (
        test_date
        if random.random() < 0.7
        else fake.date_between(
            start_date=test_date,
            end_date="+3d"
        )
    )

    rows.append([
        f"LAB{i:06}",
        random.choice(patient_ids),
        doctor,
        doctor_department[doctor],
        random.choice(tests),
        random.choice([
            "Pathology",
            "Radiology",
            "Microbiology"
        ]),
        random.choice(sample_types),
        fake.sentence(nb_words=4),
        random.choice(statuses),
        test_date,
        report_date,
        fake.sentence(nb_words=8)
    ])

columns = [
    "lab_result_id",
    "patient_id",
    "doctor_id",
    "department_id",
    "test_name",
    "test_category",
    "sample_type",
    "test_result",
    "result_status",
    "test_date",
    "report_date",
    "remarks"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "datasets/laboratory_results.csv",
    index=False
)

print(f"{len(df)} laboratory results generated successfully!")