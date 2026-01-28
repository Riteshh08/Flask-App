from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from config import Config
import app.extensions as extensions

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    # 1. Connect to Database
    client = MongoClient(app.config['MONGO_URI'])
    extensions.mongo_client = client
    extensions.db = client.get_database() 

    # 2. Register ONLY Auth Blueprint
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app