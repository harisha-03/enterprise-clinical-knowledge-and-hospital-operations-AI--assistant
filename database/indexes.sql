-- ==========================================
-- Enterprise AI Clinical Knowledge &
-- Hospital Operations Assistant
-- Database Indexes
-- ==========================================

-- Patients
CREATE INDEX idx_patients_last_name
ON patients(last_name);

CREATE INDEX idx_patients_phone
ON patients(phone);

-- Doctors
CREATE INDEX idx_doctors_department
ON doctors(department_id);

CREATE INDEX idx_doctors_specialization
ON doctors(specialization);

-- Appointments
CREATE INDEX idx_appointments_patient
ON appointments(patient_id);

CREATE INDEX idx_appointments_doctor
ON appointments(doctor_id);

CREATE INDEX idx_appointments_date
ON appointments(appointment_date);

-- Admissions
CREATE INDEX idx_admissions_patient
ON admissions(patient_id);

CREATE INDEX idx_admissions_bed
ON admissions(bed_id);

-- Laboratory Results
CREATE INDEX idx_lab_patient
ON laboratory_results(patient_id);

CREATE INDEX idx_lab_test_date
ON laboratory_results(test_date);

-- Prescriptions
CREATE INDEX idx_prescriptions_patient
ON prescriptions(patient_id);

CREATE INDEX idx_prescriptions_doctor
ON prescriptions(doctor_id);

-- Billing
CREATE INDEX idx_billing_patient
ON billing(patient_id);

CREATE INDEX idx_billing_status
ON billing(payment_status);

-- Incident Reports
CREATE INDEX idx_incident_department
ON incident_reports(department_id);

CREATE INDEX idx_incident_date
ON incident_reports(incident_date);