# coding=utf8

import openai

from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff

# 方法一，指数退避算法请求GPT，防止遇到并发瓶颈时报错
@retry(wait=wait_random_exponential(min=1, max=120), stop=stop_after_attempt(6))
def completion_with_retry(**kwargs):
    return openai.Completion.create(**kwargs)


import backoff

# 方法二，指数退避算法请求GPT，防止遇到并发瓶颈时报错
@backoff.on_exception(backoff.expo, openai.error.RateLimitError, max_time=120)
def completions_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)

