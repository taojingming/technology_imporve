from fastapi import FastAPI
import uvicorn

"""
2024-08-18 develop
"""
app = FastAPI()

@app.get('/helloworld')
async def hell_world():
    return {'msg:"hello world"'}

if __name__ == '__main__':
    uvicorn.run("helloworld:app",reload=True)