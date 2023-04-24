# coding=utf8
import fastapi
import openai
from pydantic import BaseModel

import settings
from apps.chatGPT.ai_characters import GIRLY_GIRL, TSUNDERE, SCHEMING, MUSHIN, CORKY, YANDERE, DOMINEERING_LADY
from utils.exponential_backoff import completions_with_backoff

router = fastapi.APIRouter()

gpt_model_dict = {
    'curie': 'text-curie-001',
    'davinci': 'text-davinci-003',
    'gpt-3.5-turbo': 'gpt-3.5-turbo'
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
        if model in ['text-curie-001', 'text-davinci-003']:
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

        elif model == 'gpt-3.5-turbo':
            msgs = []
            ai_profile = {"role": "system", "content": GIRLY_GIRL}
            msgs.append(ai_profile)

            dialog_ctx = msg.split('\n')
            for dia in dialog_ctx:
                if dia.startswith("YOU:"):
                    msgs.append({"role": "user", "content": dia.strip("YOU:")})
                else:
                    msgs.append({"role": "assistant", "content": dia})

            print(msgs)

            # response = openai.ChatCompletion.create(
            #     model=model,
            #     messages=msgs,
            #     temperature=0.6,
            #     max_tokens=2048,
            #     top_p=1,
            #     frequency_penalty=0,
            #     presence_penalty=0,
            # )

            response = completions_with_backoff(**dict(
                model=model,
                messages=msgs,
                temperature=0.6,
                max_tokens=2048,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            ))

            print(response)
            return {
                "status": "success",
                "msg": response.choices[0].message.content,
                "total_tokens": response['usage']['total_tokens']
            }

        else:
            raise NotImplementedError
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
    ai_profile = {"role": "system", "content": CORKY}
    msgs.append(ai_profile)

    dialog_ctx = msg.split('\n')
    for dia in dialog_ctx:
        if dia.startswith("YOU:"):
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
