-- ==========================================
-- Enterprise AI Clinical Knowledge &
-- Hospital Operations Assistant
-- Database Functions
-- ==========================================

-- ==========================================
-- Get Available Beds by Department
-- ==========================================

CREATE OR REPLACE FUNCTION get_available_beds(
    dept_id VARCHAR
)
RETURNS TABLE (
    bed_id VARCHAR,
    bed_number VARCHAR,
    room_number VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT
        b.bed_id,
        b.bed_number,
        b.room_number
    FROM beds b
    WHERE b.department_id = dept_id
      AND b.status = 'Available';
END;
$$ LANGUAGE plpgsql;


-- ==========================================
-- Count Today's Appointments
-- ==========================================

CREATE OR REPLACE FUNCTION count_today_appointments()
RETURNS INTEGER
AS $$
DECLARE
    total INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO total
    FROM appointments
    WHERE appointment_date = CURRENT_DATE;

    RETURN total;
END;
$$ LANGUAGE plpgsql;


-- ==========================================
-- Get Doctor Appointment Count
-- ==========================================

CREATE OR REPLACE FUNCTION get_doctor_appointment_count(
    doc_id VARCHAR
)
RETURNS INTEGER
AS $$
DECLARE
    total INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO total
    FROM appointments
    WHERE doctor_id = doc_id;

    RETURN total;
END;
$$ LANGUAGE plpgsql;


-- ==========================================
-- Search Patient by Phone
-- ==========================================

CREATE OR REPLACE FUNCTION search_patient_by_phone(
    patient_phone VARCHAR
)
RETURNS TABLE (
    patient_id VARCHAR,
    first_name VARCHAR,
    last_name VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.patient_id,
        p.first_name,
        p.last_name
    FROM patients p
    WHERE p.phone = patient_phone;
END;
$$ LANGUAGE plpgsql;