from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    image = request.files["image"]

    return jsonify({
        "message": "Image received",
        "analysis": "Analysis logic coming next"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
