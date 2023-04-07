# coding=utf8

import requests
import json

url = "https://open.feishu.cn/open-apis/bot/v2/hook/4e5cb008-9e92-4d4a-af85-c1ddfd473e1a"


def notify_feishu_bot(text: str):
    payload = json.dumps({
        "msg_type": "text",
        "content": {
            "text": text
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
