from brave.database import Base, Engine
import brave.database as _database, brave.modules as modules, brave.schemas as schemas
import sqlalchemy.orm as orm
import passlib.hash , bcrypt as hash_bcrypt

def create_database():
    return Base.metadata.create_all(bind=Engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_user_by_email(email: str, db: orm.Session):
    return db.query(modules.User).filter(modules.User.email == email).first()

async def create_user(users: schemas.UserCreate, db: orm.Session):
    hashed_password = hash_bcrypt.hash(users.Hashed_Pass)
    user_obj = modules.User(email=users.email, Hashed_Pass=hashed_password)
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj

# Call the function to create the database
create_database()