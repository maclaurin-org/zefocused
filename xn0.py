from flask import Flask, request, jsonify
import requests
import os  # Use environment variables for security

app = Flask(__name__)

WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Secure webhook URL
SECRET_KEY = os.getenv("SECRET_KEY")  # Secure secret key

@app.route('/send', methods=['POST'])
def send_webhook():
    data = request.json
    
    # Check if secret key is provided
    if not data or "key" not in data or data["key"] != SECRET_KEY:
        return jsonify({"error": "Unauthorized"}), 403

    # Check if "content" is present
    if "content" not in data:
        return jsonify({"error": "Invalid data"}), 400

    # Send message to Discord webhook
    response = requests.post(WEBHOOK_URL, json={"content": data["content"], "username": data.get("username", "Bot")})
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
