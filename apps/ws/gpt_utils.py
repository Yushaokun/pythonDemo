# coding=utf8
from enum import Enum

import openai

import settings

openai.api_key = settings.OPEN_API_KEY

class GPTModel(Enum):
    TextCurie001 = 1
    TextDavinci003 = 2

class GPTUtils:
    @classmethod
    def gen_echo(cls, msg: str, model_type: GPTModel = GPTModel.TextCurie001, temperature=0.9, max_tokens=200,
                 frequency_penalty=0, presence_penalty=0):
        model = 'text-ada-001'
        if model_type == GPTModel.TextCurie001:
            model = 'text-curie-001'
        elif model_type == GPTModel.TextDavinci003:
            model = 'text-davinci-003'
        else:
            pass

        try:
            response = openai.Completion.create(
                model=model,
                prompt=msg,
                temperature=temperature,
                max_tokens=max_tokens,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
            )

            print(response)
            return {
                "status": "success",
                "msg": response["choices"][0]["text"].strip(),
                "total_tokens": response['usage']['total_tokens']
            }
        except Exception as exc:
            print(exc)
            return {"status": "fail", "msg": "服务器内部出错！"}
