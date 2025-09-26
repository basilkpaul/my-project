from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

# Example environment variables for PostgreSQL connection
DB_USER = os.getenv("POSTGRES_USER", "myuser")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "mypassword")
DB_NAME = os.getenv("POSTGRES_DB", "mydb")
DB_HOST = os.getenv("DATABASE_URL", "db")  # service name in docker-compose

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/db-test")
def db_test():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return {"db_status": "ok", "result": result}
    except Exception as e:
        return {"db_status": "error", "error": str(e)}
