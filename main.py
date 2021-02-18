from typing import Optional

from fastapi import FastAPI


app = FastAPI()

# path operation decorator
@app.get("/")
# path operation function
def read_root():
    return {"Hello": "World! My first API"}


