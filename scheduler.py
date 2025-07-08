from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio

scheduler = AsyncIOScheduler()

def schedule_jobs(task):
    scheduler.add_job(task, CronTrigger(hour=7, minute=0))
    scheduler.add_job(task, CronTrigger(hour=14, minute=0))
    scheduler.add_job(task, CronTrigger(hour=22, minute=0))
    scheduler.start()
    asyncio.get_event_loop().run_forever()
