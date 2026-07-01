import pandas as pd

insurance_companies = [
    ["INS001", "Star Health", "Premium Care", 90, "1800-100-0001", "support@starhealth.com", "Active"],
    ["INS002", "Niva Bupa", "Family Health", 85, "1800-100-0002", "support@niva.com", "Active"],
    ["INS003", "ICICI Lombard", "Health Secure", 80, "1800-100-0003", "support@icici.com", "Active"],
    ["INS004", "HDFC ERGO", "Gold Plan", 75, "1800-100-0004", "support@hdfcergo.com", "Active"],
    ["INS005", "Care Health", "Comprehensive", 95, "1800-100-0005", "support@carehealth.com", "Active"],
    ["INS006", "ManipalCigna", "Health Plus", 85, "1800-100-0006", "support@manipalcigna.com", "Active"],
    ["INS007", "Aditya Birla Health", "Active Secure", 80, "1800-100-0007", "support@abhealth.com", "Active"],
    ["INS008", "SBI General", "Health Edge", 75, "1800-100-0008", "support@sbigeneral.com", "Active"],
    ["INS009", "Reliance General", "Silver Plan", 70, "1800-100-0009", "support@reliance.com", "Active"],
    ["INS010", "Bajaj Allianz", "Health Guard", 90, "1800-100-0010", "support@bajajallianz.com", "Active"],
    ["INS011", "ACKO", "Smart Health", 80, "1800-100-0011", "support@acko.com", "Active"],
    ["INS012", "Future Generali", "Family Shield", 75, "1800-100-0012", "support@futuregenerali.com", "Active"],
    ["INS013", "Universal Sompo", "Premium Plan", 85, "1800-100-0013", "support@universalsompo.com", "Active"],
    ["INS014", "Tata AIG", "Elite Care", 90, "1800-100-0014", "support@tataaig.com", "Active"],
    ["INS015", "New India Assurance", "Basic Care", 70, "1800-100-0015", "support@newindia.co.in", "Active"],
    ["INS016", "National Insurance", "Standard Plan", 75, "1800-100-0016", "support@nic.co.in", "Active"],
    ["INS017", "Oriental Insurance", "Gold Shield", 85, "1800-100-0017", "support@orientalinsurance.org.in", "Active"],
    ["INS018", "United India Insurance", "Health Protect", 80, "1800-100-0018", "support@uiic.co.in", "Active"],
    ["INS019", "Liberty General", "Wellness Plan", 85, "1800-100-0019", "support@libertyinsurance.in", "Active"],
    ["INS020", "Kotak General", "Complete Health", 90, "1800-100-0020", "support@kotak.com", "Active"]
]

columns = [
    "insurance_id",
    "provider_name",
    "plan_name",
    "coverage_percentage",
    "contact_number",
    "email",
    "status"
]

df = pd.DataFrame(insurance_companies, columns=columns)

df.to_csv(
    "datasets/insurance.csv",
    index=False
)

print("insurance.csv generated successfully!")