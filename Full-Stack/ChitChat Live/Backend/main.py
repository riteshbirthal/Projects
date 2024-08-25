from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import List, Dict
import json
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:8080", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)

class ConnectionManager:
    
    def __init__(self) -> None:
        self.active_connections: List[WebSocket] = []
        self.active_members: List[int] = []
        self.users = {}
        
        
    async def connect(self, websocket:WebSocket, client_id: int):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.active_members.append(client_id)
    
    def check_clientId(self, client_id: int):
        if client_id in manager.active_members:
            return True
        return False
    
    def write_username(self, client_id: int, username: str):
        self.users[client_id] = username
    
    def get_username(self, client_id: int):
        return self.users[client_id]
    
    
    def disconnect(self, websocket:WebSocket, client_id: int):
        self.active_connections.remove(websocket)
        self.active_members.remove(client_id)
        del self.users[client_id]
    
    
    async def send_personal_message(self, message:str, websocket:WebSocket):
        await websocket.send_text(message)
        
        
    async def broadcast(self, message:str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

@app.get("/")
async def Home():
    return "Hello Chit-Chatters!"

@app.get("/check/{client_id}")
def check_connection(client_id: int):
    return {"result" : manager.check_clientId(client_id)}



@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket:WebSocket, client_id: int):
    await manager.connect(websocket, client_id)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            if(len(data[2])):
                manager.write_username(client_id, data[1])
                message = {"time": current_time, "client_id": client_id, "username": data[1], "message": data[2], "welcome": data[3], "status": data[4]}
                await manager.broadcast(json.dumps(message))
    except WebSocketDisconnect:
        user = manager.get_username(client_id)
        manager.disconnect(websocket, client_id)
        message = {"time": current_time, "client_id": client_id, "username": "", "message": f"{user} left the chat.", "welcome": False, "status": False}
        await manager.broadcast(json.dumps(message))

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", workers=2, reload=True)