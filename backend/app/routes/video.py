from flask import Blueprint, jsonify, request
from app.models.video import Video
from app.routes.auth import token_required

video_bp = Blueprint('video', __name__)

@video_bp.route('/dashboard', methods=['GET'])
@token_required
def get_dashboard(user_id):
    # Requirement: Return exactly 2 videos
    videos = Video.get_dashboard_videos()
    
    output = []
    for v in videos:
        output.append({
            'id': v.id,
            'title': v.title,
            'description': v.description,
            'thumbnail_url': v.thumbnail_url
        })
    return jsonify(output), 200

@video_bp.route('/video/<id>/stream', methods=['GET'])
@token_required
def get_video_stream(user_id, id):
    video = Video.get_by_id(id)
    if not video:
        return jsonify({'message': 'Video not found'}), 404
    
    return jsonify({
        'youtube_id': video.youtube_id, # Return the ID, not the link
        'title': video.title
    }), 200