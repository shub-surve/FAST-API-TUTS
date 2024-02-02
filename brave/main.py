import fastapi
import sqlalchemy.orm
import brave.services as services
import brave.schemas as schemas
import brave.database as database


app = fastapi.FastAPI()

@app.post("/api/users")
async def create_user(users: schemas.UserCreate, db: sqlalchemy.orm.Session = fastapi.Depends(services.get_db)):
    db_user = await services.get_user_by_email(users.email, db)
    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="Email already in the database")

    return await services.create_user(users, db)



