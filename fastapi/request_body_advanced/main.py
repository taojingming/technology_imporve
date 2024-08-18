from fastapi import FastAPI,Path,Query,Body
import uvicorn
from typing import Optional,Set,List
from pydantic import BaseModel, Field
from enum import Enum

"""
2024-08-18 develop
"""
app = FastAPI()

class Address(BaseModel):
    address : str = Field(...,examples=['queen street'])
    postcode : str  = Field(...,examples=['7907'])
    
    model_config = {
        
        "json_schema_extra":{
            "examples": [{
                "address":'Queen street',
                "postcode":'dsd'
            }]
        }
    }

class User(BaseModel):
    username: str = Field(...,min_length=3)
    description: Optional[str] = Field(None,max_length=10)#默认为空可不写
    address : Address
    
class Feature(BaseModel):
    name:str    
     
class Item(BaseModel):
    name : str
    length : int
    features : List[Feature] 
    
# * 表示后面的参数必须关键字传递参数 如uername='fsdf'    
@app.put('/carts/{cart_id}')
async def update_cart(cart_id: int,user:User ,item:Item,count:int= Body(...,ge= 2,examples=[8])):
    print(user.username)
    print(item.name)
    result_dict ={
        "cartid":cart_id,
        "username": user.username,
        "itemname": item.name,
        "count": count
        
    } 
    return result_dict


if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)