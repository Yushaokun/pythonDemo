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


@router.websocket("/query_gpt")
async def websocket_endpoint(websocket: WebSocket):
    openai.api_key = settings.OPEN_API_KEY

    await ws_manager.connect(websocket)

    model_type = 2

    try:
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
