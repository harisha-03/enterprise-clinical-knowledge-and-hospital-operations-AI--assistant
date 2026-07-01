from sqlalchemy import text

from app.core.database import engine


class SQLExecutor:

    def execute(self, sql: str):

        sql = sql.strip()

        # Safety Checks
        if not sql.lower().startswith("select"):
            raise Exception("Only SELECT queries are allowed.")

        blocked = [
            "drop",
            "delete",
            "update",
            "insert",
            "alter",
            "truncate",
            "create"
        ]

        for keyword in blocked:
            if keyword in sql.lower():
                raise Exception(f"{keyword.upper()} statements are not allowed.")

        with engine.connect() as conn:

            result = conn.execute(text(sql))

            rows = result.mappings().all()

            return [dict(row) for row in rows]