from typing import Optional

from fastapi import FastAPI


app = FastAPI()

# path operation decorator
@app.get('/')
# path operation function
def home(limit:int,isTrue:bool):
    if isTrue:
        return {"Message":f"Welcome to our site-{limit}"} # Query parameter limit,isTrue
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

# path operation decorator
@app.get("/blog/{id}/comments") # path parameter id
# path operation function
def read_root(id:int):
    return {"Hello": id}


