import os
import requests
from flask import Flask
from telegram import Bot
from telegram.error import TelegramError

# === Настройки ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/3/3c/Piri_reis_world_map_01.jpg"
TEXT = "📌 <b>Карта, которой не должно быть</b>\n\nВ 1929 году в Турции нашли карту 1513 года, где точно изображена Антарктида безо льда... Кто мог её создать?\n\n#тайнадня #картапириреиса #антарктида"

bot = Bot(token=TELEGRAM_TOKEN)

# === Flask сервер ===
app = Flask(__name__)

@app.route("/")
def index():
    return "Бот работает. Готов к публикации!"

@app.route("/send")
def send_post():
    try:
        image_data = requests.get(IMAGE_URL).content
        bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=image_data,
            caption=TEXT,
            parse_mode="HTML"
        )
        return "✅ Пост успешно опубликован!"
    except TelegramError as e:
        return f"❌ Ошибка Telegram: {e}"
    except Exception as ex:
        return f"⚠️ Ошибка: {ex}"

# === Запуск Flask ===
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
