# coding=utf8
from fastapi import APIRouter

from .chatGPT import gpt_views

router = APIRouter()

router.include_router(gpt_views.router, prefix="/chatGPT")