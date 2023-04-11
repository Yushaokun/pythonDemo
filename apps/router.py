# coding=utf8
from fastapi import APIRouter

from .chatGPT import gpt_views
from .ws import ws_apis

router = APIRouter()

router.include_router(gpt_views.router, prefix="/chatGPT")
router.include_router(ws_apis.router, prefix="/ws")