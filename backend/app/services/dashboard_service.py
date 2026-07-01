from sqlalchemy import text
from sqlalchemy.orm import Session


def get_dashboard_overview(db: Session):

    query = text("""

        SELECT

        (SELECT COUNT(*) FROM patients) AS total_patients,

        (SELECT COUNT(*) FROM doctors) AS total_doctors,

        (SELECT COUNT(*) FROM appointments) AS total_appointments,

        (SELECT COUNT(*) FROM admissions) AS total_admissions,

        (SELECT COUNT(*) FROM laboratory_results) AS total_lab_results,

        (SELECT COUNT(*) FROM billing) AS total_bills

    """)

    result = db.execute(query).fetchone()

    return {
        "total_patients": result[0],
        "total_doctors": result[1],
        "total_appointments": result[2],
        "total_admissions": result[3],
        "total_lab_results": result[4],
        "total_bills": result[5]
    }