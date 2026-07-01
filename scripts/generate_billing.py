import random
from datetime import timedelta

import pandas as pd
from faker import Faker

fake = Faker("en_IN")

# ---------------------------------------
# Load datasets
# ---------------------------------------

patients = pd.read_csv("datasets/patients.csv")
admissions = pd.read_csv("datasets/admissions.csv")
insurance = pd.read_csv("datasets/insurance.csv")

# ---------------------------------------
# Lookup dictionaries
# ---------------------------------------

patient_insurance = dict(
    zip(
        patients["patient_id"],
        patients["insurance_id"]
    )
)

insurance_coverage = dict(
    zip(
        insurance["insurance_id"],
        insurance["coverage_percentage"]
    )
)

payment_methods = [
    "Cash",
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking"
]

payment_statuses = [
    "Paid",
    "Pending",
    "Partial"
]

rows = []

# ---------------------------------------
# Generate 15,000 bills
# ---------------------------------------

for i in range(1, 15001):

    admission = admissions.sample(n=1).iloc[0]

    patient_id = admission["patient_id"]
    admission_id = admission["admission_id"]

    insurance_id = patient_insurance[patient_id]

    coverage_percent = insurance_coverage[insurance_id]

    admission_date = pd.to_datetime(
        admission["admission_date"]
    ).date()

    bill_date = admission_date + timedelta(
        days=random.randint(0, 15)
    )

    total_amount = random.randint(2000, 300000)

    insurance_amount = round(
        total_amount * coverage_percent / 100,
        2
    )

    status = random.choices(
        payment_statuses,
        weights=[70, 20, 10],
        k=1
    )[0]

    if status == "Paid":
        amount_paid = total_amount

    elif status == "Partial":
        amount_paid = round(
            random.uniform(
                insurance_amount,
                total_amount
            ),
            2
        )

    else:
        amount_paid = 0

    rows.append([
        f"BILL{i:06}",
        patient_id,
        admission_id,
        insurance_id,
        bill_date,
        total_amount,
        insurance_amount,
        amount_paid,
        random.choice(payment_methods),
        status
    ])

columns = [
    "bill_id",
    "patient_id",
    "admission_id",
    "insurance_id",
    "bill_date",
    "total_amount",
    "insurance_coverage",
    "amount_paid",
    "payment_method",
    "payment_status"
]

df = pd.DataFrame(
    rows,
    columns=columns
)

df.to_csv(
    "datasets/billing.csv",
    index=False
)

print(f"{len(df)} billing records generated successfully!")