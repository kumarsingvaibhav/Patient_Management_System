# Configuration.py
import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Prefer environment variables so credentials are not hardcoded.
MONGO_URI = os.getenv("MONGO_URI")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

if not MONGO_URI:
    if not MONGO_PASSWORD or MONGO_PASSWORD == "YOUR_PASSWORD":
        raise RuntimeError(
            "MongoDB credentials not configured. Set MONGO_URI or MONGO_PASSWORD."
        )
    MONGO_URI = ("mongodb+srv://iamvaibhav23_db_user:nCMNLyKIRwk1zBXI@cluster0.l4oi5sx.mongodb.net/"
    ).format(password=MONGO_PASSWORD)

# Create a MongoDB client
client = MongoClient(MONGO_URI, server_api=ServerApi("1"))

# Connect to the database
db = client["Patient_db"]

# Collection for patient data
patient_collection = db["Patient_data"]
