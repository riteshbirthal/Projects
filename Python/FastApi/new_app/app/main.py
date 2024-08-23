from fastapi import FastAPI, Form
from pydantic import BaseModel
from apis.home_page import *
from models.model import *
import datetime


def include_router(app):
	app.include_router(general_pages_router)


def start_application():
	app = FastAPI()
	include_router(app)
	return app 

app = start_application()

@app.on_event("startup")
async def startup_event():
   print('Application started... :', datetime.datetime.now())
   
   
@app.on_event("shutdown")
async def shutdown_event():
   print('Application Shutdown... :', datetime.datetime.now())
   

