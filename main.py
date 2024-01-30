from fastapi import FastAPI
from core.cfg import Settings

app = FastAPI (title=Settings.PROJECT_TITLE , version = Settings.PROJECT_VERSION)

@app.get("/")

def hello():
    return{"msg":"HELLO FASTAPI"}