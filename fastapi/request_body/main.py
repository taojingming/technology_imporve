from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel
from enum import Enum

"""
2024-08-18 develop
"""
app = FastAPI()

class Gender(str ,Enum):
    male = 'male'
    female = 'female'

class UserModel(BaseModel):
    username: str
    description: Optional[str] = 'default'
    gender : Gender
     

@app.post('/users')
async def create_user(user_model : UserModel):
    print(user_model.username)
    user_dict = user_model.model_dump()
    return user_dict

@app.put('/users/{user_id}')
async def update_user(user_id:int,user_model:UserModel):
    print(user_model.username)
    user_dict = user_model.model_dump()
    user_dict.update({'id':user_id})
    
    return user_dict

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)