import pandas as pd

print("=" * 70)
print("FOREIGN KEY VALIDATION")
print("=" * 70)

patients = pd.read_csv("datasets/patients.csv")
doctors = pd.read_csv("datasets/doctors.csv")
departments = pd.read_csv("datasets/departments.csv")
beds = pd.read_csv("datasets/beds.csv")
insurance = pd.read_csv("datasets/insurance.csv")
medicines = pd.read_csv("datasets/pharmacy_inventory.csv")
admissions = pd.read_csv("datasets/admissions.csv")
nurses = pd.read_csv("datasets/nurses.csv")

appointments = pd.read_csv("datasets/appointments.csv")
lab = pd.read_csv("datasets/laboratory_results.csv")
prescriptions = pd.read_csv("datasets/prescriptions.csv")
billing = pd.read_csv("datasets/billing.csv")
discharges = pd.read_csv("datasets/discharges.csv")
incident = pd.read_csv("datasets/incident_reports.csv")

checks = [

    ("Appointments → Patients",
     appointments.patient_id.isin(patients.patient_id).all()),

    ("Appointments → Doctors",
     appointments.doctor_id.isin(doctors.doctor_id).all()),

    ("Appointments → Departments",
     appointments.department_id.isin(departments.department_id).all()),

    ("Admissions → Patients",
     admissions.patient_id.isin(patients.patient_id).all()),

    ("Admissions → Doctors",
     admissions.doctor_id.isin(doctors.doctor_id).all()),

    ("Admissions → Beds",
     admissions.bed_id.isin(beds.bed_id).all()),

    ("Discharges → Admissions",
     discharges.admission_id.isin(admissions.admission_id).all()),

    ("Lab → Patients",
     lab.patient_id.isin(patients.patient_id).all()),

    ("Lab → Doctors",
     lab.doctor_id.isin(doctors.doctor_id).all()),

    ("Lab → Departments",
     lab.department_id.isin(departments.department_id).all()),

    ("Prescriptions → Patients",
     prescriptions.patient_id.isin(patients.patient_id).all()),

    ("Prescriptions → Doctors",
     prescriptions.doctor_id.isin(doctors.doctor_id).all()),

    ("Prescriptions → Medicines",
     prescriptions.medicine_id.isin(medicines.medicine_id).all()),

    ("Billing → Patients",
     billing.patient_id.isin(patients.patient_id).all()),

    ("Billing → Admissions",
     billing.admission_id.isin(admissions.admission_id).all()),

    ("Billing → Insurance",
     billing.insurance_id.isin(insurance.insurance_id).all()),

    ("Incident → Departments",
     incident.department_id.isin(departments.department_id).all()),

    ("Incident → Doctors",
     incident.reported_by_doctor_id.isin(doctors.doctor_id).all()),

    ("Incident → Nurses",
     incident.reported_by_nurse_id.isin(nurses.nurse_id).all())
]

for name, result in checks:
    print(f"{'✅' if result else '❌'} {name}")

print("\nValidation Finished")