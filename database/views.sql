-- ==========================================
-- Enterprise AI Clinical Knowledge &
-- Hospital Operations Assistant
-- Database Views
-- ==========================================

-- ==========================================
-- Patient Summary View
-- ==========================================

CREATE OR REPLACE VIEW vw_patient_summary AS
SELECT
    p.patient_id,
    p.first_name,
    p.last_name,
    p.gender,
    p.date_of_birth,
    p.phone,
    i.provider_name AS insurance_provider
FROM patients p
LEFT JOIN insurance i
ON p.insurance_id = i.insurance_id;


-- ==========================================
-- Doctor Schedule View
-- ==========================================

CREATE OR REPLACE VIEW vw_doctor_schedule AS
SELECT
    a.appointment_id,
    a.appointment_date,
    a.appointment_time,
    d.doctor_id,
    d.first_name || ' ' || d.last_name AS doctor_name,
    p.patient_id,
    p.first_name || ' ' || p.last_name AS patient_name,
    a.status
FROM appointments a
JOIN doctors d
ON a.doctor_id = d.doctor_id
JOIN patients p
ON a.patient_id = p.patient_id;


-- ==========================================
-- Pending Laboratory Reports
-- ==========================================

CREATE OR REPLACE VIEW vw_pending_lab_reports AS
SELECT
    lab_result_id,
    patient_id,
    doctor_id,
    test_name,
    test_date,
    result_status
FROM laboratory_results
WHERE result_status = 'Pending';


-- ==========================================
-- Bed Availability View
-- ==========================================

CREATE OR REPLACE VIEW vw_bed_availability AS
SELECT
    b.bed_id,
    b.bed_number,
    b.bed_type,
    b.status,
    d.department_name
FROM beds b
JOIN departments d
ON b.department_id = d.department_id;


-- ==========================================
-- Billing Summary View
-- ==========================================

CREATE OR REPLACE VIEW vw_billing_summary AS
SELECT
    bill_id,
    patient_id,
    total_amount,
    insurance_coverage,
    amount_paid,
    balance_amount,
    payment_status
FROM billing;