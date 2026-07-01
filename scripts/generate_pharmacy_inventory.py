import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

medicine_names = [
    "Paracetamol","Amoxicillin","Azithromycin","Metformin","Amlodipine",
    "Atorvastatin","Pantoprazole","Omeprazole","Ibuprofen","Diclofenac",
    "Cetirizine","Levocetirizine","Dolo 650","Crocin","Aspirin",
    "Losartan","Telmisartan","Insulin","Cefixime","Ceftriaxone",
    "Vitamin D3","Calcium","Iron Tablets","ORS","Salbutamol",
    "Montelukast","Ondansetron","Domperidone","Rabeprazole","Ranitidine"
]

manufacturers = [
    "Sun Pharma",
    "Cipla",
    "Dr. Reddy's",
    "Lupin",
    "Mankind",
    "Torrent",
    "Alkem",
    "Abbott",
    "Pfizer",
    "GSK"
]

categories = [
    "Antibiotic",
    "Painkiller",
    "Antacid",
    "Antidiabetic",
    "Cardiology",
    "Vitamin",
    "Respiratory",
    "General Medicine"
]

dosage_forms = [
    "Tablet",
    "Capsule",
    "Injection",
    "Syrup",
    "Drops"
]

strengths = [
    "250 mg",
    "500 mg",
    "650 mg",
    "5 ml",
    "10 ml",
    "100 mg",
    "50 mg"
]

rows = []

for i in range(1,1001):

    rows.append([
        f"MED{i:05}",
        random.choice(medicine_names),
        random.choice(medicine_names),
        random.choice(manufacturers),
        random.choice(categories),
        random.choice(dosage_forms),
        random.choice(strengths),
        round(random.uniform(10,1500),2),
        random.randint(50,1000),
        random.randint(20,100),
        fake.date_between(start_date="today", end_date="+3y"),
        "Available"
    ])

columns = [
    "medicine_id",
    "medicine_name",
    "generic_name",
    "manufacturer",
    "category",
    "dosage_form",
    "strength",
    "unit_price",
    "stock_quantity",
    "reorder_level",
    "expiry_date",
    "status"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "datasets/pharmacy_inventory.csv",
    index=False
)

print("pharmacy_inventory.csv generated successfully!")