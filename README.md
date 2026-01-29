# AI-First Video App (React Native + Flask)

This is a full-stack mobile application built as a "Thin Client." The React Native frontend contains no business logic; it simply renders data provided by the Flask backend.

## 🚀 Features

- **Thin Client Architecture:** Logic resides 100% on the server.
- **Secure Authentication:** JWT-based Login/Signup (HttpOnly ready).
- **YouTube Abstraction (The Twist):** The app **never** receives raw YouTube IDs.
  - Backend generates a signed, short-lived `playback_token`.
  - Frontend exchanges this token for a stream only at the moment of playback.
- **MongoDB Integration:** Dynamic video and user storage.

## 🛠 Tech Stack

- **Frontend:** React Native (Expo), Axios
- **Backend:** Python Flask, PyMongo, PyJWT
- **Database:** MongoDB

## 📦 Setup Instructions

### 1. Backend Setup

```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt

# Create .env file with:
# MONGO_URI=mongodb://localhost:27017/Flash-App
# SECRET_KEY=your_secret_key

# Seed the database
python seed_db.py

# Run Server (Port 5001)
python run.py
```

### 2. Frontend Setup

cd frontend
npm install
npx expo start
