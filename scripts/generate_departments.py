import pandas as pd

departments = [
    ["DEP001", "Cardiology", "CARD", "Dr. Rajesh Kumar", 2, "080-10010001", "cardiology@hospital.com", "Active"],
    ["DEP002", "Neurology", "NEUR", "Dr. Priya Sharma", 3, "080-10010002", "neurology@hospital.com", "Active"],
    ["DEP003", "Orthopedics", "ORTH", "Dr. Anil Reddy", 4, "080-10010003", "orthopedics@hospital.com", "Active"],
    ["DEP004", "Emergency", "EMER", "Dr. Sneha Rao", 1, "080-10010004", "emergency@hospital.com", "Active"],
    ["DEP005", "ICU", "ICU", "Dr. Vivek Nair", 2, "080-10010005", "icu@hospital.com", "Active"],
    ["DEP006", "Pediatrics", "PED", "Dr. Kavitha Joshi", 5, "080-10010006", "pediatrics@hospital.com", "Active"],
    ["DEP007", "Radiology", "RAD", "Dr. Kiran Patel", 1, "080-10010007", "radiology@hospital.com", "Active"],
    ["DEP008", "Laboratory", "LAB", "Dr. Meera Gupta", 1, "080-10010008", "lab@hospital.com", "Active"],
    ["DEP009", "Oncology", "ONC", "Dr. Rohit Singh", 6, "080-10010009", "oncology@hospital.com", "Active"],
    ["DEP010", "General Medicine", "GEN", "Dr. Ashok Verma", 2, "080-10010010", "medicine@hospital.com", "Active"]
]

columns = [
    "department_id",
    "department_name",
    "department_code",
    "department_head",
    "floor_number",
    "phone",
    "email",
    "status"
]

df = pd.DataFrame(departments, columns=columns)

df.to_csv(
    "datasets/departments.csv",
    index=False
)

print("departments.csv generated successfully!")