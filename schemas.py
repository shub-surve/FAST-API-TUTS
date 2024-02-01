import datetime as DT
import pydantic as pydantic

class UsersBase(pydantic.BaseModel):
    email : str

class UserCreate(UsersBase):
    Hashed_Pass: str

    class Config:
        orm_mode = True

class User(UsersBase):
    id: int
    email: str

    class Config:
        orm_mode = True

class LeadBase(pydantic.BaseModel):

    first_name: str
    last_name: str
    email: str
    company: str
    note: str

class LeadCreate(LeadBase):
    pass

class Lead(LeadBase):
    id: int
    owner_id: int
    date_creates: DT.datetime
    last_update: DT.datetime

    