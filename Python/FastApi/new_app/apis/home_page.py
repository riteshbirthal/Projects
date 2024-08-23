from fastapi import APIRouter, Request, responses, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.model import *
from sqlalchemy.exc import IntegrityError
import json

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home_page.html", {"request" : request})


	