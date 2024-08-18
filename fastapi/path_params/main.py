from fastapi import FastAPI
import uvicorn
from enum import Enum
"""
2024-08-18 develop
路径参数
"""
app = FastAPI()
"""
设置 特定类型
设置枚举类型
"""
class Gender(str,Enum):
    male = 'male'
    female = 'female'

@app.get('/users/current')
async def get_current_user():
    return {'user':f'This is current user'}

@app.get('/users/{user_id}')
async def get_user(user_id:int):
    return {'user':f'This is the user for {user_id}'}

@app.get('/students/{gender}')
async def get_user(gender:Gender):
    return {'student':f'This is a for {gender.value} student'}


if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)