import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Change 5000 to 5001
    port = int(os.environ.get("PORT", 5001)) 
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("DEBUG") == "True")