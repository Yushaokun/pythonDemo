# coding=utf8

from apscheduler.schedulers.blocking import BlockingScheduler

from utils.check_gpt_tokens import gpt_detail_notify2feishu


def run_scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(gpt_detail_notify2feishu, 'interval', seconds=30)

    scheduler.start()