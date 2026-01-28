from pymongo import MongoClient

# 1. Connect to your MongoDB instance
# Make sure the database name 'video_app_db' matches your Config.py
client = MongoClient("mongodb://localhost:27017")
db = client.get_database("video_app_db")

# 2. Define the complete list of 5 videos
video_data = [
    {
        "title": "MongoDB Crash Course 2026",
        "description": "Learn MongoDB from basics to advanced in this complete crash course.",
        "youtube_id": "M1dKYQ7GsTg",
        "thumbnail_url": "https://img.youtube.com/vi/M1dKYQ7GsTg/maxresdefault.jpg",
        "is_active": True
    },
    {
        "title": "Cursor AI Tutorial",
        "description": "Personal tips and tricks for using the AI code editor efficiently.",
        "youtube_id": "rwxRoYzwkyM",
        "thumbnail_url": "https://img.youtube.com/vi/rwxRoYzwkyM/maxresdefault.jpg",
        "is_active": True
    },
    {
        "title": "Python Tutorial for Beginners",
        "description": "A complete Python course in Hindi with hand-written notes and AI integration.",
        "youtube_id": "UrsmFxEIp5k",
        "thumbnail_url": "https://img.youtube.com/vi/UrsmFxEIp5k/maxresdefault.jpg",
        "is_active": True
    },
    {
        "title": "End of Web Development?",
        "description": "An honest discussion about the future of web development in 2026.",
        "youtube_id": "xb-fcoMMiTM",
        "thumbnail_url": "https://img.youtube.com/vi/xb-fcoMMiTM/maxresdefault.jpg",
        "is_active": True
    },
    {
        "title": "5 Ways to Use AI in Coding",
        "description": "Strategies for integrating AI tools into your coding workflow.",
        "youtube_id": "CBYfXlP7ppQ",
        "thumbnail_url": "https://img.youtube.com/vi/CBYfXlP7ppQ/maxresdefault.jpg",
        "is_active": True
    }
]

# 3. Clean and Insert
# Optional: Uncomment the next line if you want to clear the collection before adding
# db.videos.delete_many({}) 

db.videos.insert_many(video_data)

print(f"Successfully added {len(video_data)} videos to the database!")