from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
db = {}

class Item(BaseModel):
    name: str
    desc: str


@app.post("/")
def create(item: Item):
    db[item.name]=item.desc
    return{"item": item}

@app.get("/")
def get_items():
    return db



