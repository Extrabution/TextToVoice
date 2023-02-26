from fastapi.templating import Jinja2Templates
from fastapi import Request, WebSocket
from services.text_to_voice_converter import convert

templates = Jinja2Templates(directory="templates")


def register(app):
    @app.get("/")
    async def index(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})

    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            data = await convert(data)
            if data is not None:
                await websocket.send_text(data)
