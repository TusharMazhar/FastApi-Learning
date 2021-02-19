from typing import Optional 

from fastapi import FastAPI

from pydantic import BaseModel 

# import uvicorn


app = FastAPI()

class Blog(BaseModel): # Blog model created/pydantic model : debug : ctrl+shift+p
    title:str
    des:str
    published:Optional[str]=None

@app.post('/')
def home(request:Blog): # use Blog model
    return {"msg":f"My blog is {request.title}"}

# path operation decorator
@app.get('/')
# path operation function
def home(limit:int,isTrue:bool,sort:Optional[str]=None):
    if isTrue:
        return {"Message":f"Welcome to our site-{limit}"} # Query parameter limit,isTrue [Example:api/?limit=12&isTrue=True]
    else:
        return {"msg":"Not valid"}

# path operation decorator
@app.get("/about/{id}")  # path parameter id
# path operation function
def read_root(id:int):
    return {"Hello": id}

# path operation decorator
@app.get("/blog/{id}/comments") # path parameter id
# path operation function
def read_root(id:int):
    return {"Hello": id}




# if __name__ = "__main__":
#     uvicorn.run(app,host="127.0.0.1",port="9000")  # Port Change