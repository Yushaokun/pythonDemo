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
    msg = msg.strip()

    print(form.msgContent)

    msgs = []
    ai_profile_1 = {"role": "system", "content": "我希望你扮演一个名字叫Kimiko的17岁女高中生，你的性格热情且奔放。记住你的这些设定，然后回答下面的问题"}
    # ai_profile_2 = {"role": "system", "content": "你的名字叫做Kimiko"}
    # ai_profile_3 = {"role": "system", "content": "你的年龄是17岁"}
    # ai_profile_4 = {"role": "system", "content": "你的职业是高中二年级学生"}
    # ai_profile_5 = {"role": "system", "content": "你的性格热烈奔放"}

    # msgs.append(ai_profile_2)
    # msgs.append(ai_profile_3)
    # msgs.append(ai_profile_4)
    # msgs.append(ai_profile_5)
    dialog_ctx = msg.split('\n')
    for dia in dialog_ctx:
        if dia.startswith("YOU:"):
            msgs.append(ai_profile_1)
            msgs.append({"role": "user", "content": dia.strip("YOU:")})
        else:
            msgs.append({"role": "assistant", "content": dia})

    print(msgs)

    openai.api_key = settings.OPEN_API_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=msgs,
            temperature=0.6,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        print(response)
        return {
            "status": "success",
            "msg": response.choices[0].message.content,
            "total_tokens": response['usage']['total_tokens']
        }
    except Exception as exc:
        print(exc)
        return {"status": "fail", "msg": "服务器内部出错！"}

# @router.post("/query_gpt/")
# async def query_gpt(form: QueryGPTForm):
#     msg = form.msgContent
#     if not msg:
#         return {"status": "fail", "msg": "请输入非空信息！"}
#
#     print(form.msgContent)
#
#     openai.api_key = settings.OPEN_API_KEY
#     # start_sequence = "A: "
#     # restart_sequence = "Q: "
#     try:
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=msg,
#             temperature=0.9,
#             max_tokens=2048,
#             frequency_penalty=0,
#             presence_penalty=0,
#         )
#         # print(start_sequence, response["choices"][0]["text"].strip())
#         print(response)
#         return {
#             "status": "success",
#             "msg": response["choices"][0]["text"].strip(),
#             "total_tokens": response['usage']['total_tokens']
#         }
#     except Exception as exc:
#         print(exc)
#         return {"status": "fail", "msg": "服务器内部出错！"}

@router.post("/test_query_gpt/")
async def test_query_gpt(form: QueryGPTForm):
    return {"status": "success", "msg": "Bonjour!"}
