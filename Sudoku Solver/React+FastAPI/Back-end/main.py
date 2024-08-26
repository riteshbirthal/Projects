from fastapi import FastAPI
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


@app.get("/")
async def Home():
    return "Welcome to Sudoku Solver Application!"

@app.get("/check")
def check_connection():
    return {"result" : 200}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", workers=2, reload=True)