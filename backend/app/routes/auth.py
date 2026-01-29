from flask import Blueprint, request, jsonify
from app.models.user import User
from app.utils.security import hash_password, check_password, generate_token
import jwt
from config import Config
from functools import wraps

auth_bp = Blueprint('auth', __name__)

# Middleware to protect the /auth/me route
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            # In a real app, you'd fetch the user from DB here
            kwargs['user_id'] = data['user_id']
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
            
        return f(*args, **kwargs)
    return decorated

@auth_bp.route('/signup', methods=['POST']) # Path updated per JD 
def signup():
    data = request.get_json()
    
    # 1. Validation includes Name per JD 
    if not data or not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Name, Email, and Password are required'}), 400

    # 2. Check if user already exists
    if User.get_by_email(data['email']):
        return jsonify({'message': 'User already exists'}), 400
        
    # 3. Create User with Name
    hashed = hash_password(data['password'])
    User.create_user(data['name'], data['email'], hashed)
    
    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing email or password'}), 400
        
    user_data = User.get_raw_by_email(data['email']) # Get full dict to check password
    
    if not user_data:
        return jsonify({'message': 'User not found'}), 404
        
    if check_password(data['password'], user_data['password']):
        token = generate_token(str(user_data['_id']))
        return jsonify({'access_token': token}), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/me', methods=['GET']) # Required profile endpoint 
@token_required
def get_profile(user_id):
    user = User.get_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
        
    # Returns Name and Email per JD
    return jsonify({
        'name': user.name,
        'email': user.email
    }), 200

@auth_bp.route('/logout', methods=['POST']) # Required per JD 
def logout():
    # Since we use JWT, we mostly handle logout on the frontend by clearing the token
    return jsonify({'message': 'Logged out successfully'}), 200