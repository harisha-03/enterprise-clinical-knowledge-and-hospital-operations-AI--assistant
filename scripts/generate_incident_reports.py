import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

# ---------------------------------------
# Load datasets
# ---------------------------------------

departments = pd.read_csv("datasets/departments.csv")
doctors = pd.read_csv("datasets/doctors.csv")
nurses = pd.read_csv("datasets/nurses.csv")

incident_types = [
    "Medication Error",
    "Patient Fall",
    "Equipment Failure",
    "Needle Stick Injury",
    "Wrong Patient Identification",
    "Delay in Treatment",
    "Laboratory Error",
    "Fire Safety Incident",
    "Data Privacy Incident",
    "Patient Complaint"
]

severity_levels = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

statuses = [
    "Open",
    "Under Investigation",
    "Resolved",
    "Closed"
]

rows = []

for i in range(1, 5001):

    department = departments.sample(1).iloc[0]
    dept_id = department["department_id"]

    dept_doctors = doctors[
        doctors["department_id"] == dept_id
    ]

    dept_nurses = nurses[
        nurses["department_id"] == dept_id
    ]

    doctor_id = (
        dept_doctors.sample(1).iloc[0]["doctor_id"]
        if not dept_doctors.empty
        else None
    )

    nurse_id = (
        dept_nurses.sample(1).iloc[0]["nurse_id"]
        if not dept_nurses.empty
        else None
    )

    incident_date = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    rows.append([
        f"INC{i:05}",
        dept_id,
        doctor_id,
        nurse_id,
        random.choice(incident_types),
        random.choice(severity_levels),
        incident_date,
        fake.time_object().strftime("%H:%M:%S"),
        fake.paragraph(nb_sentences=2),
        fake.sentence(nb_words=8),
        random.choice(statuses)
    ])

columns = [
    "incident_id",
    "department_id",
    "reported_by_doctor_id",
    "reported_by_nurse_id",
    "incident_type",
    "severity",
    "incident_date",
    "incident_time",
    "description",
    "action_taken",
    "status"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "datasets/incident_reports.csv",
    index=False
)

print(f"{len(df)} incident reports generated successfully!")