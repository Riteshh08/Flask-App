import jwt
import datetime
from config import Config
from app.extensions import db
from bson.objectid import ObjectId

# Re-exporting existing auth functions so imports elsewhere don't break
from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    return generate_password_hash(password)

def check_password(password, hashed):
    return check_password_hash(hashed, password)

def generate_token(user_id):
    # This is your existing Auth Token logic
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

# --- NEW: OPTION B IMPLEMENTATION ---

def generate_playback_token(video_id_str, youtube_id):
    """
    Generates a short-lived token specifically for playing a video.
    This hides the youtube_id inside the token payload.
    """
    payload = {
        'video_db_id': video_id_str,
        'youtube_id': youtube_id, # Encrypted inside the token
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10) # Short expiry
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

def decode_playback_token(token, video_db_id):
    """
    Verifies the token is valid, not expired, and matches the requested video.
    """
    try:
        data = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        
        # Ensure this token was meant for THIS specific video database ID
        if data.get('video_db_id') != video_db_id:
            return None
            
        return data.get('youtube_id')
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None