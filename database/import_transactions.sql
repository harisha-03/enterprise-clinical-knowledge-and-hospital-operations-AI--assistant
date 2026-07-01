\copy admissions(admission_id,patient_id,doctor_id,bed_id,admission_date,admission_time,admission_reason,admission_type,expected_discharge_date,status) FROM 'C:/Users/mmhar/OneDrive/Desktop/hospital-ai-assistant/datasets/admissions.csv' CSV HEADER;

\copy appointments(appointment_id,patient_id,doctor_id,department_id,appointment_date,appointment_time,appointment_type,reason_for_visit,status) FROM 'C:/Users/mmhar/OneDrive/Desktop/hospital-ai-assistant/datasets/appointments.csv' CSV HEADER;

\copy discharges(discharge_id,admission_id,patient_id,discharge_date,discharge_time,discharge_summary,discharge_status,follow_up_date) FROM 'C:/Users/mmhar/OneDrive/Desktop/hospital-ai-assistant/datasets/discharges.csv' CSV HEADER;

\copy laboratory_results(lab_result_id,patient_id,doctor_id,department_id,test_name,test_category,sample_type,test_result,result_status,test_date,report_date,remarks) FROM 'C:/Users/mmhar/OneDrive/Desktop/hospital-ai-assistant/datasets/laboratory_results.csv' CSV HEADER;

\copy prescriptions(prescription_id,patient_id,doctor_id,medicine_id,dosage,frequency,duration_days,quantity,instructions,prescription_date) FROM 'C:/Users/mmhar/OneDrive/Desktop/hospital-ai-assistant/datasets/prescriptions.csv' CSV HEADER;

\copy billing(bill_id,patient_id,admission_id,insurance_id,bill_date,total_amount,insurance_coverage,amount_paid,payment_method,payment_status) FROM 'C:/Users/mmhar/OneDrive/Desktop/hospital-ai-assistant/datasets/billing.csv' CSV HEADER;

\copy incident_reports(incident_id,department_id,reported_by_doctor_id,reported_by_nurse_id,incident_type,severity,incident_date,incident_time,description,action_taken,status) FROM 'C:/Users/mmhar/OneDrive/Desktop/hospital-ai-assistant/datasets/incident_reports.csv' CSV HEADER;