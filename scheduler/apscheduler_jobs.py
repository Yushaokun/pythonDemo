# coding=utf8
from apscheduler.schedulers.background import BackgroundScheduler

from utils.check_gpt_tokens import gpt_detail_notify2feishu


def run_scheduler():
    scheduler = BackgroundScheduler()

    # 同步定时任务
    scheduler.add_job(gpt_detail_notify2feishu, 'interval', seconds=60 * 60 * 3)

    scheduler.start()
