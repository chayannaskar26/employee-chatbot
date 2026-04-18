# main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from chain.main_chain import runChain

app = FastAPI()

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()

            # runChain('what is the mission and vision of this company?')
            response = runChain(data.lower())

            await websocket.send_text(response)

    except WebSocketDisconnect:
        print("Client disconnected")

app.mount("/", StaticFiles(directory="frontend", html=True), name="index")