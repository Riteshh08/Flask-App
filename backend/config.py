import os
from dotenv import load_dotenv

load_dotenv() # Load variables from .env

class Config:
    # Use the environment variable, or fallback to a default if missing
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/Flas-App')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_key')