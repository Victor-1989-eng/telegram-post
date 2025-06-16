# main.py
import os
import requests
from flask import Flask, request
from telegram import Bot
from telegram.error import TelegramError

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=TELEGRAM_TOKEN)

@app.route("/send", methods=["GET"])
def send_post():
    try:
        image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3c/Piri_reis_world_map_01.jpg"
        text = (
            "📍 <b>Карта, которой не должно быть</b>\n\n"
            "В 1929 году в Турции нашли карту 1513 года, где точно изображена Антарктида безо льда... "
            "Кто мог её создать?\n\n"
            "#тайнадня #картапириреиса #антарктида"
        )

        image_data = requests.get(image_url).content

        bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=image_data,
            caption=text,
            parse_mode="HTML"
        )
        return "✅ Пост отправлен!", 200

    except TelegramError as e:
        return f"❌ Ошибка Telegram: {e}", 500
    except Exception as ex:
        return f"⚠️ Ошибка: {ex}", 500
