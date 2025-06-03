from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7557395751:AAHAqIZJZ-wsy2P1rIZbZgHg_bzLSuspsgk'
CHAT_ID = '1825511235'

@app.route("/sms", methods=["POST"])
def receive_sms():
    data = request.json
    sender = data.get("from", "Неизвестно")
    message = data.get("message", "")

    text = f"📩 Новое СМС от {sender}:\n\n{message}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # берем порт из Render или 8080 по умолчанию
    app.run(host="0.0.0.0", port=port)
