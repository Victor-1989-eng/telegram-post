import os
import requests
from flask import Flask
from telegram import Bot
from telegram.error import TelegramError

# === Инициализация Flask ===
app = Flask(__name__)

# === Настройки ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Токен Telegram-бота
CHANNEL_ID = os.getenv("CHANNEL_ID")          # Например: @arhiv_tayn

# Пример данных поста (можно потом заменять)
IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/3/3c/Piri_reis_world_map_01.jpg"
TEXT = """📍 <b>Карта, которой не должно быть</b>

В 1929 году в Турции нашли карту 1513 года, где точно изображена Антарктида безо льда... Кто мог её создать?

#тайнадня #картапириреиса #антарктида"""

# === Инициализация бота ===
bot = Bot(token=TELEGRAM_TOKEN)


# === Главная страница ===
@app.route("/")
def index():
    return "🤖 Бот работает. Готов к публикации!"


# === Ручной запуск поста ===
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
        return "✅ Пост опубликован!"
    except TelegramError as e:
        return f"❌ Ошибка Telegram: {e}"
    except Exception as ex:
        return f"⚠️ Общая ошибка: {ex}"


# === Запуск сервера ===
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Используем порт, выданный Render
    app.run(host="0.0.0.0", port=port)
