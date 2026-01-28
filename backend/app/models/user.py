from app.extensions import db

class User:
    def __init__(self, user_data):
        self.id = str(user_data.get('_id'))
        self.email = user_data.get('email')
        self.password = user_data.get('password')

    @staticmethod
    def get_by_email(email):
        user_data = db.users.find_one({"email": email})
        return User(user_data) if user_data else None

    @staticmethod
    def create_user(email, hashed_password):
        db.users.insert_one({
            "email": email,
            "password": hashed_password
        })