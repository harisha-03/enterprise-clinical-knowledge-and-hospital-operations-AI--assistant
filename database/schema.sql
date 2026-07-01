-- ==========================================
-- Enterprise AI Clinical Knowledge &
-- Hospital Operations Assistant
-- Database Schema
-- ==========================================

--- DROP DATABASE IF EXISTS hospital_ai;

---CREATE DATABASE hospital_ai;

---\c hospital_ai;

-- ==========================================
-- Patients Master Table
-- ==========================================

CREATE TABLE patients (
    patient_id VARCHAR(15) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10),
    date_of_birth DATE,
    blood_group VARCHAR(5),
    phone VARCHAR(15),
    email VARCHAR(100),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(15),
    insurance_id VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- ==========================================
-- Departments Master Table
-- ==========================================

CREATE TABLE departments (
    department_id VARCHAR(15) PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    department_code VARCHAR(10) UNIQUE NOT NULL,
    department_head VARCHAR(100),
    floor_number INT,
    phone VARCHAR(15),
    email VARCHAR(100),
    status VARCHAR(20) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);




-- ==========================================
-- Doctors Master Table
-- ==========================================

CREATE TABLE doctors (
    doctor_id VARCHAR(15) PRIMARY KEY,
    department_id VARCHAR(15) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    qualification VARCHAR(100),
    experience_years INT,
    phone VARCHAR(15),
    email VARCHAR(100) UNIQUE,
    consultation_fee DECIMAL(10,2),
    status VARCHAR(20) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_doctor_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


-- ==========================================
-- Nurses Master Table
-- ==========================================

CREATE TABLE nurses (
    nurse_id VARCHAR(15) PRIMARY KEY,
    department_id VARCHAR(15) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    qualification VARCHAR(100),
    experience_years INT,
    shift VARCHAR(20),
    phone VARCHAR(15),
    email VARCHAR(100) UNIQUE,
    status VARCHAR(20) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_nurse_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


-- ==========================================
-- Insurance Master Table
-- ==========================================

CREATE TABLE insurance (
    insurance_id VARCHAR(15) PRIMARY KEY,
    provider_name VARCHAR(100) NOT NULL,
    plan_name VARCHAR(100) NOT NULL,
    coverage_percentage DECIMAL(5,2),
    contact_number VARCHAR(15),
    email VARCHAR(100),
    status VARCHAR(20) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- ==========================================
-- Beds Master Table
-- ==========================================

CREATE TABLE beds (
    bed_id VARCHAR(15) PRIMARY KEY,
    department_id VARCHAR(15) NOT NULL,
    bed_number VARCHAR(20) NOT NULL UNIQUE,
    bed_type VARCHAR(30) NOT NULL,
    room_number VARCHAR(20),
    floor_number INT,
    status VARCHAR(20) DEFAULT 'Available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_bed_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


-- ==========================================
-- Operation Theatres Master Table
-- ==========================================

CREATE TABLE operation_theatres (
    theatre_id VARCHAR(15) PRIMARY KEY,
    department_id VARCHAR(15) NOT NULL,
    theatre_name VARCHAR(100) NOT NULL,
    theatre_number VARCHAR(20) UNIQUE NOT NULL,
    floor_number INT,
    theatre_type VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_theatre_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


-- ==========================================
-- Pharmacy Inventory Master Table
-- ==========================================

CREATE TABLE pharmacy_inventory (
    medicine_id VARCHAR(15) PRIMARY KEY,
    medicine_name VARCHAR(100) NOT NULL,
    generic_name VARCHAR(100),
    manufacturer VARCHAR(100),
    category VARCHAR(50),
    dosage_form VARCHAR(50),
    strength VARCHAR(50),
    unit_price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    reorder_level INT DEFAULT 50,
    expiry_date DATE,
    status VARCHAR(20) DEFAULT 'Available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ==========================================
-- Appointments Transaction Table
-- ==========================================

CREATE TABLE appointments (
    appointment_id VARCHAR(15) PRIMARY KEY,
    patient_id VARCHAR(15) NOT NULL,
    doctor_id VARCHAR(15) NOT NULL,
    department_id VARCHAR(15) NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    appointment_type VARCHAR(30),
    reason_for_visit TEXT,
    status VARCHAR(20) DEFAULT 'Scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_appointment_patient
        FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id),

    CONSTRAINT fk_appointment_doctor
        FOREIGN KEY (doctor_id)
        REFERENCES doctors(doctor_id),

    CONSTRAINT fk_appointment_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- ==========================================
-- Admissions Transaction Table
-- ==========================================

CREATE TABLE admissions (
    admission_id VARCHAR(15) PRIMARY KEY,
    patient_id VARCHAR(15) NOT NULL,
    doctor_id VARCHAR(15) NOT NULL,
    bed_id VARCHAR(15) NOT NULL,
    admission_date DATE NOT NULL,
    admission_time TIME NOT NULL,
    admission_reason TEXT,
    admission_type VARCHAR(30),
    expected_discharge_date DATE,
    status VARCHAR(20) DEFAULT 'Admitted',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_admission_patient
        FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id),

    CONSTRAINT fk_admission_doctor
        FOREIGN KEY (doctor_id)
        REFERENCES doctors(doctor_id),

    CONSTRAINT fk_admission_bed
        FOREIGN KEY (bed_id)
        REFERENCES beds(bed_id)
);


-- ==========================================
-- Discharges Transaction Table
-- ==========================================

CREATE TABLE discharges (
    discharge_id VARCHAR(15) PRIMARY KEY,
    admission_id VARCHAR(15) NOT NULL,
    patient_id VARCHAR(15) NOT NULL,
    discharge_date DATE NOT NULL,
    discharge_time TIME NOT NULL,
    discharge_summary TEXT,
    discharge_status VARCHAR(30),
    follow_up_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_discharge_admission
        FOREIGN KEY (admission_id)
        REFERENCES admissions(admission_id),

    CONSTRAINT fk_discharge_patient
        FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id)
);


-- ==========================================
-- Laboratory Results Transaction Table
-- ==========================================

CREATE TABLE laboratory_results (
    lab_result_id VARCHAR(15) PRIMARY KEY,
    patient_id VARCHAR(15) NOT NULL,
    doctor_id VARCHAR(15) NOT NULL,
    department_id VARCHAR(15) NOT NULL,
    test_name VARCHAR(100) NOT NULL,
    test_category VARCHAR(50),
    sample_type VARCHAR(50),
    test_result TEXT,
    result_status VARCHAR(30) DEFAULT 'Pending',
    test_date DATE NOT NULL,
    report_date DATE,
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_lab_patient
        FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id),

    CONSTRAINT fk_lab_doctor
        FOREIGN KEY (doctor_id)
        REFERENCES doctors(doctor_id),

    CONSTRAINT fk_lab_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


-- ==========================================
-- Prescriptions Transaction Table
-- ==========================================

CREATE TABLE prescriptions (
    prescription_id VARCHAR(15) PRIMARY KEY,
    patient_id VARCHAR(15) NOT NULL,
    doctor_id VARCHAR(15) NOT NULL,
    medicine_id VARCHAR(15) NOT NULL,
    dosage VARCHAR(100) NOT NULL,
    frequency VARCHAR(100) NOT NULL,
    duration_days INT NOT NULL,
    quantity INT NOT NULL,
    instructions TEXT,
    prescription_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_prescription_patient
        FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id),

    CONSTRAINT fk_prescription_doctor
        FOREIGN KEY (doctor_id)
        REFERENCES doctors(doctor_id),

    CONSTRAINT fk_prescription_medicine
        FOREIGN KEY (medicine_id)
        REFERENCES pharmacy_inventory(medicine_id)
);


-- ==========================================
-- Billing Transaction Table
-- ==========================================

CREATE TABLE billing (
    bill_id VARCHAR(15) PRIMARY KEY,
    patient_id VARCHAR(15) NOT NULL,
    admission_id VARCHAR(15),
    insurance_id VARCHAR(15),
    bill_date DATE NOT NULL,
    total_amount DECIMAL(12,2) NOT NULL,
    insurance_coverage DECIMAL(12,2) DEFAULT 0,
    amount_paid DECIMAL(12,2) DEFAULT 0,
    balance_amount DECIMAL(12,2) GENERATED ALWAYS AS (total_amount - insurance_coverage - amount_paid) STORED,
    payment_method VARCHAR(30),
    payment_status VARCHAR(20) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_billing_patient
        FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id),

    CONSTRAINT fk_billing_admission
        FOREIGN KEY (admission_id)
        REFERENCES admissions(admission_id),

    CONSTRAINT fk_billing_insurance
        FOREIGN KEY (insurance_id)
        REFERENCES insurance(insurance_id)
);

-- ==========================================
-- Incident Reports Transaction Table
-- ==========================================

CREATE TABLE incident_reports (
    incident_id VARCHAR(15) PRIMARY KEY,
    department_id VARCHAR(15) NOT NULL,
    reported_by_doctor_id VARCHAR(15),
    reported_by_nurse_id VARCHAR(15),
    incident_type VARCHAR(100) NOT NULL,
    severity VARCHAR(20),
    incident_date DATE NOT NULL,
    incident_time TIME NOT NULL,
    description TEXT,
    action_taken TEXT,
    status VARCHAR(20) DEFAULT 'Open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_incident_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id),

    CONSTRAINT fk_incident_doctor
        FOREIGN KEY (reported_by_doctor_id)
        REFERENCES doctors(doctor_id),

    CONSTRAINT fk_incident_nurse
        FOREIGN KEY (reported_by_nurse_id)
        REFERENCES nurses(nurse_id)
);