from fastapi import FastAPI,Path,Query,Body,Response,Cookie,Header
import uvicorn
from typing import Optional,Set,List, Union
from pydantic import BaseModel, Field
from enum import Enum

"""
2024-08-18 develop
"""
app = FastAPI()
    
# * 表示后面的参数必须关键字传递参数 如uername='fsdf'    
@app.put('/carts')
async def update_cart(*,
                      response: Response ,
                      favorite_schema:Optional[str] = Cookie(...,alias='favorite-schema'),
                      api_token:Union[str,None] = Header(...,alias="api-token")):
    result_dict = {
        
        "favorite_schema": favorite_schema,
        "api_token": api_token
    }
    
    response.set_cookie(key="favorite_schema",value="light")
    return result_dict


if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)