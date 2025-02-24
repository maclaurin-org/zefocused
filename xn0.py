from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Your actual Discord webhook
SECRET_KEY = os.getenv("SECRETKEY")  # The secret key from Render

@app.route('/send', methods=['POST'])
def send_webhook():
    data = request.json
    auth_header = request.headers.get("Authorization")

    # 🔒 Check if the secret key matches
    if auth_header != SECRET_KEY:
        return jsonify({"error": "Unauthorized"}), 403

    # 🔍 Validate data
    if not data or "content" not in data:
        return jsonify({"error": "Invalid data"}), 400

    # 🚀 Send request to Discord
    response = requests.post(WEBHOOK_URL, json=data)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
