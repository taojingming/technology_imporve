from typing import Optional,Set,List, Union
from pydantic import BaseModel, Field
from enum import Enum
import uvicorn
from fastapi import FastAPI,Path,HTTPException,status,Request,Response
from fastapi.responses import JSONResponse



users = {
    "a": {"id":1, "username":"a"},
    "b": {"id":2, "username":"b", "password":"bbb"},
    "c": {"id":3, "username":"c", "password":"ccc", "description": "default"},
    "d": {"id":4, "username":"d", "password":"ddd", "description": "user add"},
    "e": {"id":5, "username":"e", "password":"eee", "description": "user eee", "fullname": "Mary Water"
          }   
}
app =FastAPI()

class UserBase(BaseModel):
    id: Optional[int] = None
    username: str
    fullname: Optional[str] = None
    description: Optional[str] = None

class UserOut(BaseModel):
      ...

class ErrorMessage(BaseModel):
    error_code: int
    message: str

class UserIn(UserBase):
    password: str

#自定义异常的类型
class UserNotFoundException(Exception):
    def __init__(self, username:str) :
        self.username = username
       
# 非正常结束约束采用responses
@app.post('/users', status_code=201,response_model=UserOut,responses={
    400:{'model':ErrorMessage},
    401:{'model':ErrorMessage},
    
})
async def create_user(user: UserIn):
    
    if users.get(user.username, None):
        error_messgae = ErrorMessage(error_code=400, message=f'{user.username} already exists')
        return JSONResponse(status_code=400,content=error_messgae.model_dump())
    user_dict = user.model_dump()
    user_dict.update({"id": 10})
    
    return user_dict    

#detail 补充说明，status.HTTP_404_NOT_FOUND 自带的状态码类型
@app.get('/users/{username}',status_code=200,response_model=UserOut)
async def get_user(username:str = Path(...,min_length=1)):
    user = users.get(username,None)
    if user:
        return user
    
    #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{username} not found')
    raise UserNotFoundException(username)

@app.exception_handler(UserNotFoundException)
async def user_not_found_exception_handler(request:Request,exc:UserNotFoundException):
    return JSONResponse(status_code=404, content={
        
        'error_code':404,
        'message': f'{exc.username} not found',
        'info': 'fsdfds'
            
    }
                        )
    
if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)