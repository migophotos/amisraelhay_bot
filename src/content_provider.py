import aiogram.exceptions
from datetime import datetime, timedelta

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from shared.config import Config
from database.sql import DataBase
from database.user_info import UserInfo


class ContentProvider:
    users_list = []

    def __init__(self, bot: Bot):
        self.bot = bot
        self.jobId = ""
        self.jobObj = 0
        self.scheduler = AsyncIOScheduler(timezone="Asia/Jerusalem")
        self.scheduler.start()

        self.broadcast_to_users_jobId = ""
        self.broadcast_to_users_jobObj = 0

    async def start_update_broadcast(self):
        db: DataBase = self.bot.db

        if len(ContentProvider.users_list) == 0:
            ContentProvider.users_list = await db.get_users()

        self.broadcast_to_users_jobId = "update-" + str(id(datetime.now()))
        self.broadcast_to_users_jobObj = self.scheduler.add_job(self.broadcast_to_users,
                                                                id=self.broadcast_to_users_jobId, trigger='cron',
                                                                name="broadcast_to_users", second="*/2",
                                                                start_date=datetime.now())

        return self.broadcast_to_users_jobObj.next_run_time

    async def broadcast_to_users(self):
        if len(ContentProvider.users_list) > 0:
            id, name, lang, _ = ContentProvider.users_list.pop()
            if id != Config.admin_id:
                text = self.bot.ml.msg("update_db_msg", lang).format(name)
                try:
                    await self.bot.send_message(id, text=text)
                except aiogram.exceptions.Any as err:
                    await self.bot.send_message(Config.admin_id, text=f"Error to send update message to {name}: {id}")
                finally:
                    await self.bot.send_message(Config.admin_id, text=f"Update sent to {name}: {id}")
        else:
            if self.broadcast_to_users_jobId:
                self.scheduler.remove_job(self.broadcast_to_users_jobId)
                self.broadcast_to_users_jobId = ''
                await self.bot.send_message(Config.admin_id, text=f"Broadcast to users done")

    def is_broadcast_to_users(self):
        return bool(self.broadcast_to_users_jobId)

    def is_running(self):
        return bool(self.jobId)

    async def stop_scheduler(self):
        if self.jobId:
            self.scheduler.remove_job(self.jobId)
            self.jobId = ''
            return 'stopped'
        return 'not running'

    async def restart_scheduler(self):
        db: DataBase = self.bot.db
        sched = await db.get_scheduler()
        month = sched[0] if len(sched[0]) else None
        day = sched[1] if len(sched[1]) else None
        dow = sched[2] if len(sched[2]) else None
        hour = sched[3] if len(sched[3]) else None
        minute = sched[4] if len(sched[4]) else None
        jitter = int(sched[5]) if len(sched[5]) else None

        if self.jobId:
            self.scheduler.remove_job(self.jobId)
            self.jobId = ''

        self.jobId = str(id(datetime.now()))
        self.jobObj = self.scheduler.add_job(self.send_message, id=self.jobId, trigger='cron', month=month, day=day,
                                             day_of_week=dow, hour=hour, minute=minute, jitter=jitter,
                                             start_date=datetime.now())
        return self.jobObj.next_run_time

    async def send_message(self):
        print("send message")



