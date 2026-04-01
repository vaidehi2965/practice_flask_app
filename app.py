from flask import Flask, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_data(endpoint):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@app.route("/")
def home():
    return {"message": "Flask API Wrapper for JSONPlaceholder"}


@app.route("/posts")
def get_posts():
    data = fetch_data("posts")
    return jsonify(data)


@app.route("/comments")
def get_comments():
    data = fetch_data("comments")
    return jsonify(data)


@app.route("/albums")
def get_albums():
    data = fetch_data("albums")
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)