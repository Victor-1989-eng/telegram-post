import os
import asyncio
import requests
from datetime import datetime
from telegram import Bot
from telegram.error import TelegramError
from flask import Flask

# === НАСТРОЙКИ ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/3/3c/Piri_reis_world_map_01.jpg"
TEXT = (
    "📌 <b>Карта, которой не должно быть</b>\n\n"
    "В 1929 году в Турции нашли карту 1513 года, где точно изображена Антарктида безо льда... "
    "Кто мог её создать?\n\n"
    "#тайнадня #картапириреиса #антарктида"
)

bot = Bot(token=TELEGRAM_TOKEN)
app = Flask(__name__)

async def send_post():
    try:
        image_data = requests.get(IMAGE_URL).content
        await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=image_data,
            caption=TEXT,
            parse_mode="HTML"
        )
        print("✅ Пост успешно отправлен")
    except TelegramError as e:
        print(f"❌ Ошибка Telegram: {e}")
    except Exception as ex:
        print(f"⚠️ Общая ошибка: {ex}")

@app.route('/send')
def manual_trigger():
    asyncio.run(send_post())  # <-- Ждём выполнения
    return "Пост отправлен (если без ошибок)"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
