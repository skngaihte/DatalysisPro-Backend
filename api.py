from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route("/api/data")
def get_data():
    return {"message": "Hello from backend!"}

if __name__ == "__main__":
    app.run()