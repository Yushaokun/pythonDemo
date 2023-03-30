# coding=utf8
import fastapi
from starlette.websockets import WebSocket, WebSocketDisconnect

from ws.utils import ConnectionManager

router = fastapi.APIRouter()

manager = ConnectionManager()

@router.websocket("/test/{user}")
async def websocket_endpoint(websocket: WebSocket, user: str):

    await manager.connect(websocket)

    await manager.broadcast(f"用户{user}进入聊天室")

    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"你说了: {data}", websocket)
            await manager.broadcast(f"用户:{user} 说: {data}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"用户-{user}-离开")