from app.extensions import db
from bson.objectid import ObjectId
from datetime import datetime

class User:
    def __init__(self, user_data):
        self.id = str(user_data.get('_id'))
        self.name = user_data.get('name') # Added name per JD 
        self.email = user_data.get('email')
        self.password = user_data.get('password')
        self.created_at = user_data.get('created_at') # Added timestamp per JD 

    @staticmethod
    def get_by_email(email):
        user_data = db.users.find_one({"email": email})
        return User(user_data) if user_data else None

    @staticmethod
    def get_raw_by_email(email):
        # Returns the raw dictionary for password verification in auth routes
        return db.users.find_one({"email": email})

    @staticmethod
    def get_by_id(user_id):
        # Required for the /auth/me endpoint to fetch profile by JWT ID
        try:
            user_data = db.users.find_one({"_id": ObjectId(user_id)})
            return User(user_data) if user_data else None
        except:
            return None

    @staticmethod
    def create_user(name, email, hashed_password):
        # Includes name and created_at per requirements
        db.users.insert_one({
            "name": name,
            "email": email,
            "password": hashed_password,
            "created_at": datetime.utcnow()
            
        })