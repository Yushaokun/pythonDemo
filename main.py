# coding=utf8
import sys

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from apps.router import router
from scheduler.apscheduler_jobs import run_scheduler
from settings import ENABLE_SCHEDULER

app = fastapi.FastAPI()
app.include_router(router)

# 挂载静态资源
app.mount('/static', StaticFiles(directory='static'), name='static')

if __name__ == '__main__':
    if ENABLE_SCHEDULER:
        run_scheduler()

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8010
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    uvicorn.run(app="main:app", host="127.0.0.1", port=port, workers=workers)
