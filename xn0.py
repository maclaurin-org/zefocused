from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1342837328011460731/l0ZnsTLQTe_sOe6QwrSrKoGShFqkeO7lBJcBHJibd1ASQ_yqZlr1_65xOq8ZMJzmn5k1"

@app.route('/send', methods=['POST'])
def send_webhook():
    data = request.json
    if not data or "content" not in data:
        return {"error": "Invalid data"}, 400
    response = requests.post(WEBHOOK_URL, json=data)
    return response.json(), response.status_code

app.run(host='0.0.0.0', port=8080)
