from flask import Blueprint, jsonify, request
from app.models.video import Video
from app.routes.auth import token_required
# Import the new helper functions
from app.utils.security import generate_playback_token, decode_playback_token

video_bp = Blueprint('video', __name__)

@video_bp.route('/dashboard', methods=['GET'])
@token_required
def get_dashboard(user_id):
    videos = Video.get_dashboard_videos()
    
    output = []
    for v in videos:
        # Generate the abstraction token
        playback_token = generate_playback_token(v.id, v.youtube_id)

        output.append({
            'id': v.id,
            'title': v.title,
            'description': v.description,
            'thumbnail_url': v.thumbnail_url,
            'token': playback_token # Send token INSTEAD of youtube_id
        })
    
    return jsonify(output), 200

@video_bp.route('/video/<id>/stream', methods=['GET'])
@token_required
def get_video_stream(user_id, id):
    # 1. Extract the token from query params
    token = request.args.get('token')
    
    if not token:
        return jsonify({'message': 'Missing playback token'}), 400

    # 2. Decode and Validate
    # We verify the token matches the requested video ID
    hidden_youtube_id = decode_playback_token(token, id)
    
    if not hidden_youtube_id:
        return jsonify({'message': 'Invalid or expired token'}), 403

    # 3. Return the "Stream" (In this case, the unlocked ID)
    # This fulfills Option B: The app requested with a token, we verified, and now provide access.
    return jsonify({
        'stream_id': hidden_youtube_id 
    }), 200