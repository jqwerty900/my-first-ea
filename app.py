from flask import Flask, jsonify
from bot import analyze_market

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

@app.route("/signal")
def signal():
    decision = analyze_market()
    return jsonify({"signal": decision})

if __name__ == "__main__":
    app.run()
