from fastapi import FastAPI
import uvicorn
from typing import Optional

"""
2024-08-18 develop
"""
app = FastAPI()

@app.get('/users')
async def get_users(page_index:int,page_size:Optional[int] = 30):
    return {'page info':f'index:{page_index},size:{page_size}'}

@app.get('/users/{user_id}/friends')
async def get_users(page_index:int,user_id:int,page_size:Optional[int] = 10):
    return {'user friends':f'user id:{user_id},index:{page_index},size:{page_size}'}

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)