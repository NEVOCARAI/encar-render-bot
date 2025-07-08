import os
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from encar_parser import fetch_recent_cars
from dotenv import load_dotenv
import asyncio

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

def format_price(krw):
    return f"{krw:,} KRW"

async def post_car_data():
    cars = await fetch_recent_cars()
    if not cars:
        await bot.send_message(CHANNEL_ID, "❌ Нет новых объявлений.")
        return

    for car in cars:
        text = (
            f"<b>🚗 {car['title']}</b>\n"
            f"💰 Цена: {format_price(car['price_krw'])}\n"
            f"📅 Дата публикации: {car['date']}\n"
            f"🏷️ Марка: {car['brand']}\n\n"
            f"<b>Описание:</b> {car['description']}\n"
            f"🔗 Encar: {car['link']}\n"
            f"👨‍🔧 @nevocarai"
        )
        try:
            if car['image_url']:
                await bot.send_photo(CHANNEL_ID, photo=car['image_url'], caption=text)
            else:
                await bot.send_message(CHANNEL_ID, text)
        except Exception:
            await bot.send_message(CHANNEL_ID, text)

        await asyncio.sleep(2)
