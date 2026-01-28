from flask import Blueprint, request, jsonify
from app.models.user import User
from app.utils.security import hash_password, check_password, generate_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validation
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email and Password are required'}), 400

    # Check if user already exists
    if User.get_by_email(data['email']):
        return jsonify({'message': 'User already exists'}), 400
        
    # Create User
    hashed = hash_password(data['password'])
    User.create_user(data['email'], hashed)
    
    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing data'}), 400
        
    user = User.get_by_email(data['email'])
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
        
    if check_password(data['password'], user.password):
        token = generate_token(user.id)
        return jsonify({'access_token': token}), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401