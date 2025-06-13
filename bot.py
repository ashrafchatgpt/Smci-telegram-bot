import requests
import json
from datetime import datetime

def load_config():
    with open("smci_bot_config.json") as f:
        return json.load(f)

config = load_config()
bot_token = config["bot_token"]
chat_id = config["chat_id"]

def get_stock_data():
    return {
        "date": datetime.now().strftime("%d %b %Y"),
        "close": 43.36,
        "high": 44.08,
        "low": 42.32,
        "volume": "24.7M"
    }

def format_message(data):
    return f"""
📊 SMCI – Daily Update | {data['date']}
• Closed at ${data['close']} (+0.35%)
• Range: ${data['low']} – ${data['high']}
• Volume: {data['volume']}
✅ Support held. Swing range intact.
"""

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

def main():
    send_telegram_message(format_message(get_stock_data()))

if __name__ == "__main__":
    main()
