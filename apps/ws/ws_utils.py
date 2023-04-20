# coding=utf8
import json
from typing import List

from starlette.websockets import WebSocket

from apps.ws.gpt_utils import GPTUtils, GPTModelType


class WebSocketClient:
    ws_id: str
    ws: WebSocket


class GPTWebSocketClient(WebSocketClient):
    model_type: GPTModelType

    def __init__(self, ws_id: str, ws: WebSocket, model_type: GPTModelType = GPTModelType.TextCurie001):
        self.ws_id = ws_id
        self.ws = ws
        self.model_type = model_type


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# 单例类
class ConnectionManager(metaclass=Singleton):
    def __init__(self):
        # 存放激活的ws连接对象
        self.active_connections: List[WebSocket] = []

    async def connect(self, ws: WebSocket):
        # 等待连接
        await ws.accept()
        # 存储ws连接对象
        self.active_connections.append(ws)

    def disconnect(self, ws: WebSocket):
        # 关闭时 移除ws对象
        self.active_connections.remove(ws)

    # @staticmethod
    async def send_message(self, message: str, ws: WebSocket):
        # 发送个人消息
        await ws.send_text(message)

    async def maintain_gpt_conn(self, ws_client: GPTWebSocketClient):
        websocket, ws_id, model_type = ws_client.ws, ws_client.ws_id, ws_client.model_type

        while True:
            rec_json = await websocket.receive_json()

            if rec_json == 'pong':
                continue

            rec_msg = rec_json.get('msgContent', '')

            if not rec_msg:
                return {"status": "fail", "msg": "请输入非空信息！"}
            print(rec_msg)

            echo_msg = GPTUtils.gen_echo(msg=rec_msg, model_type=model_type)
            echo_msg_json = json.dumps(echo_msg)
            await self.send_message(echo_msg_json, websocket)

    async def broadcast(self, message: str):
        # 广播消息
        for connection in self.active_connections:
            await connection.send_text(message)


# 发送ping-pong
async def ws_keep_alive():
    print("send ping...")
    cm = ConnectionManager()
    await cm.broadcast('ping')