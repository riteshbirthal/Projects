from fastapi import APIRouter, Request, responses, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.model import *
from sqlalchemy.exc import IntegrityError
import json

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()

def read_users_data():
    users = []
    with open('users_data.json', 'r') as openfile:
        json_object = json.load(openfile)
        for obj in json_object["users"]:
            users.append(User(id=obj["id"], name=obj["name"], age=obj["age"]))
    return users


users = read_users_data()

def write_data():
    global users
    temp_data = []
    for data in users:
        temp = {"id" : data.id, "name" : data.name, "age" : data.age}
        temp_data.append(temp)
    json_object = json.dumps({"users": temp_data}, indent=4)
    with open("users_data.json", "w") as outfile:
        outfile.write(json_object)


def add_user(user : User):
    global users
    users.append(user)
    temp_data = []
    for data in users:
        temp = {"id" : data.id, "name" : data.name, "age" : data.age}
        temp_data.append(temp)
    json_object = json.dumps({"users": temp_data}, indent=4)
    with open("users_data.json", "w") as outfile:
        outfile.write(json_object)


@general_pages_router.get("/update-user/{user_id}")
async def update_user(request : Request, user_id : int):
    user = {}
    for usr in users:
        if usr.id == user_id:
            user = usr
    return templates.TemplateResponse("user_form.html", {"request" : request, "form" : "update", "user" : user})


@general_pages_router.post("/update-user/{user_id}")
async def update_user(request: Request, user_id : int):
    global users
    temp = users
    temp = [user for user in temp if user.id!=user_id]
    form = UserCreateForm(request, temp)
    await form.load_data()
    if await form.is_valid():
        users = temp
        user = User( id=form.id, name=form.name, age=form.age)
        try:
            # print(user)
            add_user(user)
            return responses.RedirectResponse("/", status_code=status.HTTP_302_FOUND)
        except IntegrityError:
            form.__dict__.get("errors").append("Invalid data")
            return templates.TemplateResponse("user_form.html", form.__dict__)
    return templates.TemplateResponse("user_form.html", form.__dict__)


@general_pages_router.get("/delete-user/{user_id}")
async def delete_user(request: Request, user_id : int):
    global users
    users = [user for user in users if user.id!=user_id]
    temp_data = []
    for data in users:
        temp = {"id" : data.id, "name" : data.name, "age" : data.age}
        temp_data.append(temp)
    json_object = json.dumps({"users": temp_data}, indent=4)
    with open("users_data.json", "w") as outfile:
        outfile.write(json_object)
    return responses.RedirectResponse("/", status_code=status.HTTP_302_FOUND)


@general_pages_router.get("/")
async def home(request: Request):
    users_data = users
    return templates.TemplateResponse("home_page.html", {"request" : request, "users": users_data})


@general_pages_router.get("/users/{user_id}")
async def user_details(request: Request, user_id : int):
    user_data = {}
    for obj in users:
        if obj.id == int(user_id):
            user_data = obj
    flag = False
    if user_data:
        flag = True
    return templates.TemplateResponse("user.html", { "request" : request, "user" : user_data, "flag": flag})


@general_pages_router.get("/create_user")
async def user_details(request: Request):
    return templates.TemplateResponse("user_form.html", {"request" : request, "form" : "create"})


@general_pages_router.post("/create_user")
async def user_details(request: Request):
    form = UserCreateForm(request, users)
    await form.load_data()
    if await form.is_valid():
        user = User( id=form.id, name=form.name, age=form.age)
        try:
            print(user)
            add_user(user)
            return responses.RedirectResponse("/", status_code=status.HTTP_302_FOUND)
        except IntegrityError:
            form.__dict__.get("errors").append("Invalid data")
            return templates.TemplateResponse("user_form.html", {"request" : request , "user" : user, "form" : "create", "invalid" : True, "errors": form.__dict__.get("errors")})
    user = User(id=form.id, name=form.name, age=form.age)
    return templates.TemplateResponse("user_form.html", {"request" : request , "user" : user, "form" : "create", "invalid" : True, "errors": form.__dict__.get("errors")})


	