import os
import time
import requests
from datetime import datetime

# === НАСТРОЙКИ ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # пример: @Arxiv_tain
IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/3/3c/Piri_reis_world_map_01.jpg"
TEXT = "🗺 <b>Карта, которой не должно быть</b>\n\nВ 1929 году в Турции нашли карту 1513 года, где точно изображена Антарктида безо льда... Кто мог её создать?\n\n#тайнадня #картапириреиса #антарктида"
SEND_HOUR = 7  # 7:00 утра

def send_post():
    try:
        # Скачиваем изображение
        image_data = requests.get(IMAGE_URL).content

        # Сохраняем во временный файл
        with open("image.jpg", "wb") as f:
            f.write(image_data)

        # Отправляем запрос Telegram API
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
        with open("image.jpg", "rb") as img:
            response = requests.post(url, data={
                "chat_id": CHANNEL_ID,
                "caption": TEXT,
                "parse_mode": "HTML"
            }, files={"photo": img})

        if response.status_code == 200:
            print("✅ Пост отправлен")
        else:
            print("❌ Ошибка при отправке:", response.text)

    except Exception as e:
        print("⚠️ Ошибка:", e)

# === ЦИКЛ ОЖИДАНИЯ ===
while True:
    now = datetime.now()
    if now.hour == SEND_HOUR and now.minute == 0:
        send_post()
        time.sleep(60)
    time.sleep(20)
