import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/pricing_db")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "5000"))
