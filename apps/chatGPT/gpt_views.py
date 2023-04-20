# coding=utf8
import fastapi
import openai
from pydantic import BaseModel

import settings

router = fastapi.APIRouter()

gpt_model_dict = {
    'curie': 'text-curie-001',
    'davinci': 'text-davinci-003'
}

class QueryGPTForm(BaseModel):
    msgContent: str = None

@router.post("/query_gpt_by_name/{model_name}")
async def query_gpt_by_name(form: QueryGPTForm, model_name: str):
    msg = form.msgContent
    if not msg:
        return {"status": "fail", "msg": "请输入非空信息！"}

    print(form.msgContent)

    model = gpt_model_dict.get(model_name, 'text-curie-001')
    openai.api_key = settings.OPEN_API_KEY

    try:
        response = openai.Completion.create(
            model=model,
            prompt=msg,
            temperature=0.9,
            max_tokens=2048,
            frequency_penalty=0,
            presence_penalty=0,
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
            # model="text-curie-001",
            model="text-davinci-003",
            prompt=msg,
            temperature=0.9,
            max_tokens=200,
            frequency_penalty=0,
            presence_penalty=0,
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
