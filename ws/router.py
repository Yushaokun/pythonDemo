# coding=utf8
from fastapi import APIRouter

from ws import gpt_ws

router = APIRouter()

router.include_router(gpt_ws.router, prefix="/ws")