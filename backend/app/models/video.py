from app.extensions import db
from bson.objectid import ObjectId

class Video:
    def __init__(self, video_data):
        self.id = str(video_data.get('_id'))
        self.title = video_data.get('title')
        self.description = video_data.get('description')
        self.youtube_id = video_data.get('youtube_id')
        self.thumbnail_url = video_data.get('thumbnail_url')
        self.is_active = video_data.get('is_active', True)

    @staticmethod
    def get_dashboard_videos():
        # Requirement: Returns 2 videos only
        videos_cursor = db.videos.find({"is_active": True}).limit(2)
        return [Video(v) for v in videos_cursor]

    @staticmethod
    def get_by_id(video_id):
        try:
            data = db.videos.find_one({"_id": ObjectId(video_id)})
            return Video(data) if data else None
        except:
            return None