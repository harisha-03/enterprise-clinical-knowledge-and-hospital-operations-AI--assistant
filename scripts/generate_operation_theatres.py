import random
import pandas as pd

departments = [
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

theatre_types = [
    "General Surgery",
    "Cardiac Surgery",
    "Neurosurgery",
    "Orthopedic Surgery",
    "Emergency Surgery"
]

status = [
    "Available",
    "Occupied",
    "Maintenance"
]

rows = []

for i in range(1, 26):

    rows.append([
        f"OT{i:03}",
        random.choice(departments),
        f"Operation Theatre {i}",
        f"OT-{i:02}",
        random.randint(1,6),
        random.choice(theatre_types),
        random.choice(status)
    ])

columns = [
    "theatre_id",
    "department_id",
    "theatre_name",
    "theatre_number",
    "floor_number",
    "theatre_type",
    "status"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "datasets/operation_theatres.csv",
    index=False
)

print("operation_theatres.csv generated successfully!")