# coding=utf8
import fastapi
import openai
from starlette.websockets import WebSocket, WebSocketDisconnect

import settings
from apps.ws.utils import ConnectionManager

router = fastapi.APIRouter()

manager = ConnectionManager()

@router.websocket("/query_gpt")
async def websocket_endpoint(websocket: WebSocket):
    openai.api_key = settings.OPEN_API_KEY

    await manager.connect(websocket)

    try:
        while True:
            rec_msg = await websocket.receive_text()
            if not rec_msg:
                return {"status": "fail", "msg": "请输入非空信息！"}
            print(rec_msg)

            echo_msg = ''
            await manager.send_message(echo_msg, websocket)
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)

    except Exception as exc:
        print(exc)
        return {"status": "fail", "msg": "服务器内部出错！"}