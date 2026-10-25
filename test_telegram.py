import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_test_alert():
    message = (
        "🤖 *Dual-Agent System Online!*\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "✅ Telegram Bridge: Connected\n"
        "🟡 Gold Agent: Ready\n"
        "🛢️ Oil Agent: Ready\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "Testing connection successful."
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(
                "✅ Message sent successfully! Apna Telegram check karo."
            )
        else:
            print(
                f"❌ Error aaya (Status Code {response.status_code}): {response.text}"
            )
    except Exception as e:
        print(f"❌ Connection fail hua: {e}")


if __name__ == "__main__":
    send_test_alert()
  
