from typing import Optional,Set,List, Union
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from enum import Enum
import uvicorn
from fastapi import FastAPI,Depends, Header
import sys,jwt
from fastapi import FastAPI,Path,HTTPException,status,Request,Response
from datetime import datetime,timedelta,timezone

SECURITY_KEY = "fsdfgdghfhgjhukyhuikl"
ALGORITHMS = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

class Token(BaseModel):
    access_token: str
    token_type : str
    
    
app = FastAPI()    

def validate_user(username:str,password:str):
    if username == 'Jack' and password == '111':
        return username
    
    return None


def get_current_username(token: str = Depends(oauth2_scheme)):
    unauth_exp = HTTPException(status_code=401,detail ="UNauthorized")
    try:
        username =None
        token_data = jwt.decode(token,SECURITY_KEY,ALGORITHMS)
        if token_data:
            username = token_data.get("username",None)
            
    except Exception as error:
        raise unauth_exp
    
    if not username:
        raise unauth_exp
    
    return username         

@app.post('/token')
async def login(login_form: OAuth2PasswordRequestForm = Depends()):
    username = validate_user(login_form.username,login_form.password)
    if not username:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate":"Bearer"}
        )
  # 有效时间
    token_expries = datetime.now(timezone.utc)+timedelta(minute=300)
    token_data = {
        "username": username,
        "exp": token_expries
        
    }
    
    token = jwt.encode(token_data,SECURITY_KEY,ALGORITHMS)
    
    return Token(access_token= token, token_type="bearer")


@app.get('/items')
async def get_item(username: str = Depends(get_current_username)):
    return {"current user":username}

if __name__ == '__main__':

    uvicorn.run("main:app",reload=True)