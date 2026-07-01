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

bed_types = [
    "General",
    "Private",
    "Semi-Private",
    "ICU"
]

status = [
    "Available",
    "Occupied",
    "Maintenance"
]

rows = []

for i in range(1, 501):

    rows.append([
        f"BED{i:04}",
        random.choice(departments),
        f"B{i:04}",
        random.choice(bed_types),
        f"R-{random.randint(100,599)}",
        random.randint(1,6),
        random.choice(status)
    ])

columns = [
    "bed_id",
    "department_id",
    "bed_number",
    "bed_type",
    "room_number",
    "floor_number",
    "status"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "datasets/beds.csv",
    index=False
)

print("beds.csv generated successfully!")