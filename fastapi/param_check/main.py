from enum import Enum
import uvicorn
from fastapi import FastAPI ,Path,Query

"""
2024-08-18 develop
"""
app = FastAPI()

#query param  1 表示默认，非必须参数 ，alias 别名 为了适应语法问题，可以在传入参数中又称
@app.get('/users')
async def get_users(page_index : int = Query(1,alias='page-index' ,title='Page Index',ge=1,le=1000)):
    
    return {'user':f' page_index : {page_index}'}
    

#... 表示是必须有，必须要输出，内容不管
@app.get('/users/{user_id}')
async def get_users(user_id : int = Path(...,title='User ID',ge=1,le=1000)):
   
    return {'user':f'This is the user for {user_id}'}

@app.get('/books/{book_name}')
async def get_book(book_name : str = Path(...,title='Book Name',min_length=1,max_length=100)):
   
    return {'user':f'This is the user for {book_name}'}
#正则化约束参数
@app.get('/items/{item_no}')#a-7890
async def get_book(item_no : str = Path(...,title='Item No',regex='^[a|b|c|]-[\\d]*$')):
    return {'user':f'This is the user for {item_no}'}


if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)