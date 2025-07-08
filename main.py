import asyncio
from post_bot import post_car_data
from scheduler import schedule_jobs

if __name__ == "__main__":
    print("📅 Планировщик запущен. Ждём времени публикации...")
    schedule_jobs(post_car_data)
