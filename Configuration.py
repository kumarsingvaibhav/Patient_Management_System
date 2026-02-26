import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv() 

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise RuntimeError("Set MONGO_URI environment variable")

client = MongoClient(MONGO_URI, server_api=ServerApi("1"))

db = client["Patient_db"]
patient_collection = db["Patient_data"]