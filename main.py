import os
import time
import requests
from datetime import datetime
from telegram import Bot
from telegram.error import TelegramError

# === НАСТРОЙКИ ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # будет задана в Render
CHANNEL_ID = os.getenv("CHANNEL_ID")  # формат: @your_channel_username
IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/3/3c/Piri_reis_world_map_01.jpg"  # пример
TEXT = (
    "📌 <b>Карта, которой не должно быть</b>\n\n"
    "В 1929 году в Турции нашли карту 1513 года, где точно изображена Антарктида безо льда... "
    "Кто мог её создать?\n\n#тайнадня #картапириреиса #антарктида"
)
SEND_HOUR = 7  # Время отправки — 7:00

bot = Bot(token=TELEGRAM_TOKEN)


def send_post():
    try:
        image_data = requests.get(IMAGE_URL).content

        bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=image_data,
            caption=TEXT,
            parse_mode="HTML"
        )
        print("✅ Пост отправлен")

    except TelegramError as e:
        print(f"❌ Ошибка Telegram: {e}")
    except Exception as ex:
        print(f"⚠️ Общая ошибка: {ex}")


# === ЦИКЛ ОЖИДАНИЯ ===
while True:
    now = datetime.now()
    if now.hour == SEND_HOUR and now.minute == 0:
        send_post()
        time.sleep(60)  # чтобы не отправить дважды
    time.sleep(20)  # проверяем каждые 20 сек
    
