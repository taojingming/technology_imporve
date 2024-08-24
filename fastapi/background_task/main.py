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

app = FastAPI()

def send_messgage(msg:str):
    print(f'start sending "{msg}')
    time.sleep(10)
    print(f'complete sending "{msg}')
    
    return True

@app.post('/notify')
async def send_notification(messgae:str,background_task:BackgroundTasks):
    background_tasks.add_task(send_message,msg=message)
    
    return {"msssage": f'sending notification {message} in background'}


if __name__ == '__main__':

    uvicorn.run("main:app",reload=True)    





if __name__ == '__main__':

    uvicorn.run("main:app",reload=True)