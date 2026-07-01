from sqlalchemy import text

from app.core.database import engine

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))

        print("\n✅ Connected Successfully!\n")
        print(result.fetchone()[0])

except Exception as e:
    print("\n❌ Connection Failed\n")
    print(e)