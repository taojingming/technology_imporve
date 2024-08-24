from typing import Optional,Set,List, Union
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from enum import Enum
import uvicorn
from fastapi import FastAPI,Depends, Header
import sys,jwt
from fastapi import FastAPI,Path,HTTPException,status,Request,Response,BackgroundTasks
from datetime import datetime,timedelta,timezone
from sqlalchemy import create_engine,String,Integer,select,asc, update
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped,mapped_column
import time



title = "My Fastapi learning project"
description = "This is my first learning project API for fastapi"
version = "1.0"
terms_of_service = 'http://hifenge.com'
contact = {
    "name":"Jack Ma",
    "url":"http://hifenge.com",
    "email":"jack@hifenge.com"
}
#api 标签
tags_metdata = [
    {
        "name":"books",
        "description":"APIs for book management",
        "externalDocxs":{
            "description":"Books info for external",
            "url":"http://hifenge.com"
            
        }
    },
    {
        
        "name":"users",
        "description":"APIs for user management"
    }
    
    
]

app = FastAPI(title=title,
              description=description,
              version=version,
              terms_of_service=terms_of_service,
              contact=contact,
              openapi_tags=tags_metdata,
              openapi_url='/docs/v1/docs.json',
              resoc_url = "/ddd",
              docs_url="/ui")

@app.post('/books')
async def get_books():
    return {"books":f"Here's all books info"}

@app.post('/users')
async def get_users():
    return {"users":f"Here's all users info"}



if __name__ == '__main__':

    uvicorn.run("main:app",reload=True)    
