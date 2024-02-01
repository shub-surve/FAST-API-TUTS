from fastapi import FastAPI, HTTPException, applications , status , Depends


develop_db = ["DB for Development"]

app = FastAPI()

def get_db_session():
    return develop_db

@app.post("/items")
def add_items(item: str, db = Depends(get_db_session)):
    db.append(item)
    print(db)
    return{"message": f"added item {item}"}