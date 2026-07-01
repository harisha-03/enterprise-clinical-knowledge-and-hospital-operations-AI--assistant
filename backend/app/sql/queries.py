QUERIES = {

    "icu_beds": """
        SELECT COUNT(*) AS total
        FROM beds
        WHERE LOWER(bed_type)='icu'
        AND LOWER(status)='available';
    """

}