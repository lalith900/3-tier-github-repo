from flask import Flask
from dotenv import load_dotenv
import os
import psycopg2
import redis

load_dotenv()

app = Flask(__name__)

# PostgreSQL connection
db_connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

# Redis connection
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    decode_responses=True
)


@app.route("/")
def home():
    return {"message": "Backend Running"}


@app.route("/health")
def health():
    return {"status": "healthy"}


@app.route("/db-check")
def db_check():
    cursor = db_connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()

    return {
        "database": "connected",
        "postgres_version": db_version[0]
    }


@app.route("/redis-check")
def redis_check():
    redis_client.set("test_key", "Redis Working")

    value = redis_client.get("test_key")

    return {
        "redis": value
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec B104
