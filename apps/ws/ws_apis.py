# coding=utf8
import uuid

import fastapi
import openai
from starlette.websockets import WebSocket, WebSocketDisconnect

import settings
from apps.ws.gpt_utils import GPTModelType
from apps.ws.ws_utils import ConnectionManager, GPTWebSocketClient

router = fastapi.APIRouter()

ws_manager = ConnectionManager()


@router.websocket("/query_gpt/{model_type}")
async def websocket_endpoint(websocket: WebSocket, model_type: int):
    openai.api_key = settings.OPEN_API_KEY

    await ws_manager.connect(websocket)

    try:
        # while True:
        #     rec_msg = await websocket.receive_text()
        #     if not rec_msg:
        #         return {"status": "fail", "msg": "请输入非空信息！"}
        #     print(rec_msg)
        #
        #     echo_msg = ''
        #     await ws_manager.send_message(echo_msg, websocket)

        print(f"GPT Model Type: {model_type}")

        await ws_manager.maintain_gpt_conn(GPTWebSocketClient(
            ws_id=str(uuid.uuid4()).replace('-', ''),
            ws=websocket,
            model_type=GPTModelType(model_type))
        )

    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)

    except Exception as exc:
        print(exc)
        return {"status": "fail", "msg": "服务器内部出错！"}
