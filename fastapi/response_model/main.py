from typing import Optional,Set,List, Union
from pydantic import BaseModel, Field
from enum import Enum
import uvicorn
from fastapi import FastAPI
import sys


users = {
    "a": {"id":1, "username":"a"},
    "b": {"id":2, "username":"b", "password":"bbb"},
    "c": {"id":3, "username":"c", "password":"ccc", "description": "default"},
    "d": {"id":4, "username":"d", "password":"ddd", "description": "user add"},
    "e": {"id":5, "username":"e", "password":"eee", "description": "user eee", "fullname": "Mary Water"
          }   
}
app =FastAPI()

class UserOut(BaseModel):
    id: int
    username: str
    description :Optional[str] = "default"
# response_model_exclude = {"id"} 除了这几个都要
# response_model_include={"id","useranme"} 只要这几个参数
# response_model_exclude_unset=True 没有设置的参数不要  
@app.get('/users/{username}',response_model=UserOut,response_model_exclude_unset=True )
async def get_user(username:str):
    return users.get(username, {})

@app.get('/users',response_model=List[UserOut])
async def get_users():
    return users.values()
    
if __name__ == '__main__':
    print(sys.executable)
    uvicorn.run("main:app",reload=True)