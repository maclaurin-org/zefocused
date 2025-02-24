from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Secure webhook

@app.route('/send', methods=['POST'])
def send_webhook():
    data = request.get_json()  # Ensure it's parsed as JSON
    print("Received data:", data)  # Debugging

    if not data or "content" not in data:
        print("❌ Invalid Data")
        return jsonify({"error": "Invalid data"}), 400  # Error if content is missing

    headers = {"Content-Type": "application/json"}
    response = requests.post(WEBHOOK_URL, json=data, headers=headers)

    print("✅ Discord Response:", response.text)  # Log Discord's response
    return response.json(), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Render default port
