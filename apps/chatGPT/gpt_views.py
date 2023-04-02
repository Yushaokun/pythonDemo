# coding=utf8
import fastapi
import openai
from pydantic import BaseModel

import settings

router = fastapi.APIRouter()

class QueryGPTForm(BaseModel):
    msgContent: str = None

@router.post("/query_gpt/")
async def query_gpt(form: QueryGPTForm):
    msg = form.msgContent
    if not msg:
        return {"status": "fail", "msg": "请输入非空信息！"}

    print(form.msgContent)

    openai.api_key = settings.OPEN_API_KEY
    # start_sequence = "A: "
    # restart_sequence = "Q: "
    try:
        response = openai.Completion.create(
            model="text-curie-001",
            # model="text-davinci-003",
            prompt=msg,
            temperature=0.9,
            max_tokens=200,
            frequency_penalty=0,
            presence_penalty=0
        )
        # print(start_sequence, response["choices"][0]["text"].strip())
        print(response)
        return {
            "status": "success",
            "msg": response["choices"][0]["text"].strip(),
            "total_tokens": response['usage']['total_tokens']
        }
    except Exception as exc:
        print(exc)
        return {"status": "fail", "msg": "服务器内部出错！"}

@router.post("/query_gpt_davinci/")
async def query_gpt(form: QueryGPTForm):
    msg = form.msgContent
    if not msg:
        return {"status": "fail", "msg": "请输入非空信息！"}

    print(form.msgContent)

    openai.api_key = settings.OPEN_API_KEY
    # start_sequence = "A: "
    # restart_sequence = "Q: "
    try:
        response = openai.Completion.create(
            # model="text-curie-001",
            model="text-davinci-003",
            prompt=msg,
            temperature=0.9,
            max_tokens=200,
            frequency_penalty=0,
            presence_penalty=0
        )
        # print(start_sequence, response["choices"][0]["text"].strip())
        print(response)
        return {
            "status": "success",
            "msg": response["choices"][0]["text"].strip(),
            "total_tokens": response['usage']['total_tokens']
        }
    except Exception as exc:
        print(exc)
        return {"status": "fail", "msg": "服务器内部出错！"}

@router.post("/query_gpt_curie/")
async def query_gpt(form: QueryGPTForm):
    msg = form.msgContent
    if not msg:
        return {"status": "fail", "msg": "请输入非空信息！"}

    print(form.msgContent)

    openai.api_key = settings.OPEN_API_KEY
    # start_sequence = "A: "
    # restart_sequence = "Q: "
    try:
        response = openai.Completion.create(
            model="text-curie-001",
            # model="text-davinci-003",
            prompt=msg,
            temperature=0.9,
            max_tokens=200,
            frequency_penalty=0,
            presence_penalty=0
        )
        # print(start_sequence, response["choices"][0]["text"].strip())
        print(response)
        return {
            "status": "success",
            "msg": response["choices"][0]["text"].strip(),
            "total_tokens": response['usage']['total_tokens']
        }
    except Exception as exc:
        print(exc)
        return {"status": "fail", "msg": "服务器内部出错！"}

@router.post("/test_query_gpt/")
async def test_query_gpt(form: QueryGPTForm):
    return {"status": "success", "msg": "Bonjour!"}
    # msg = form.msgContent
    # if not msg:
    #     return {"status": "fail", "msg": "请输入非空信息！"}
    #
    # openai.api_key = settings.OPEN_API_KEY
    # # start_sequence = "A: "
    # # restart_sequence = "Q: "
    # try:
    #     response = openai.Completion.create(
    #         model="text-davinci-003",
    #         prompt=msg,
    #         temperature=0.9,
    #         max_tokens=2000,
    #         frequency_penalty=0,
    #         presence_penalty=0
    #     )
    #     # print(start_sequence, response["choices"][0]["text"].strip())
    #     return {"status": "success", "msg": response["choices"][0]["text"].strip()}
    # except Exception as exc:
    #     print(exc)
    #     return {"status": "fail", "msg": "服务器内部出错！"}
