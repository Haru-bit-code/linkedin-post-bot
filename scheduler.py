from main import run
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

scheduler.add_job(
    run,
    'cron',
    hour=9,
    minute=0
)

scheduler.start()