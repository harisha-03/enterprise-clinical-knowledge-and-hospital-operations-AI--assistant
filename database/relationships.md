# Entity Relationships

patients
├── appointments
├── admissions
├── discharges
├── laboratory_results
├── prescriptions
└── billing

doctors
├── appointments
├── prescriptions
└── departments

departments
├── doctors
├── nurses
├── beds
└── operation_theatres

admissions
├── beds
└── discharges
