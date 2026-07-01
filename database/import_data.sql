\copy doctors(doctor_id,department_id,first_name,last_name,specialization,qualification,experience_years,phone,email,consultation_fee,status) FROM 'C:/Users/mmhar/OneDrive/Desktop/hospital-ai-assistant/datasets/doctors.csv' CSV HEADER;

\copy nurses(nurse_id,department_id,first_name,last_name,qualification,experience_years,shift,phone,email,status) FROM 'C:/Users/mmhar/OneDrive/Desktop/hospital-ai-assistant/datasets/nurses.csv' CSV HEADER;

\copy beds(bed_id,department_id,bed_number,bed_type,room_number,floor_number,status) FROM 'C:/Users/mmhar/OneDrive/Desktop/hospital-ai-assistant/datasets/beds.csv' CSV HEADER;

\copy operation_theatres(theatre_id,department_id,theatre_name,theatre_number,floor_number,theatre_type,status) FROM 'C:/Users/mmhar/OneDrive/Desktop/hospital-ai-assistant/datasets/operation_theatres.csv' CSV HEADER;

\copy patients(patient_id,first_name,last_name,gender,date_of_birth,blood_group,phone,email,address,city,state,country,emergency_contact_name,emergency_contact_phone,insurance_id) FROM 'C:/Users/mmhar/OneDrive/Desktop/hospital-ai-assistant/datasets/patients.csv' CSV HEADER;