from pydantic import BaseModel
from typing import List, Optional
from fastapi import Request

class User(BaseModel):
    id : int
    name : str
    age : int
    
class UserCreateForm():
    def __init__(self, request : Request, users : list):
        self.request: Request = request
        self.errors: List = []
        self.id: Optional[int] = None
        self.name: Optional[str] = None
        self.age: Optional[int] = None
        self.user_ids: list = []
        for obj in users:
            self.user_ids.append(obj.id)
        
    async def load_data(self):
        form = await self.request.form()
        self.id = int(form.get("id"))
        self.name = form.get("name")
        self.age = int(form.get("age"))
        
    async def is_valid(self):
        if not self.id:
            self.errors.append("ID not provided")
        elif self.id in self.user_ids:
            self.errors.append("This ID has already been used. Please try again with different id.")
        if not self.name or not len(self.name) > 2:
            self.errors.append("Name should have > 2 chars")
        if not self.age or self.age<=0 or self.age>120:
            self.errors.append("Provide valid age.")
        if not self.errors:
            return True
        return False