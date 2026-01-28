import os

class Config:
    # Security Key (keep this secret in production)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-123'
    
    # MongoDB Connection URI
    # If you are using a local MongoDB, use this:
    MONGO_URI = "mongodb://localhost:27017/video_app_db"
    
    # If you are using MongoDB Atlas (Cloud), paste your connection string above instead.