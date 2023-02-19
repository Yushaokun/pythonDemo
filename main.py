# coding=utf8
import fastapi
import uvicorn

from apps.router import router
app = fastapi.FastAPI()
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="127.0.0.1", port=8888, reload=True)
