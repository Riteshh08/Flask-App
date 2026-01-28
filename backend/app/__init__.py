from flask import Flask, request, make_response
from flask_cors import CORS
from pymongo import MongoClient
from config import Config
import app.extensions as extensions

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # 1. Broad CORS for local development
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    # 2. Preflight Handler
    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            response = make_response()
            response.headers.add("Access-Control-Allow-Origin", "*")
            response.headers.add('Access-Control-Allow-Headers', "*")
            response.headers.add('Access-Control-Allow-Methods', "*")
            return response

    # 3. Database Connection
    client = MongoClient(app.config['MONGO_URI'])
    extensions.mongo_client = client
    extensions.db = client.get_database() 

    # 4. Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.video import video_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth') # mandatory /auth prefix
    app.register_blueprint(video_bp) # Reachable at /dashboard

    return app