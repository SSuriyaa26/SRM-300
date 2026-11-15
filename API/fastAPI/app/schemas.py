import datetime

from pydantic import  BaseModel,EmailStr,ConfigDict
class PostBase(BaseModel):
    title: str
    content: str
    published:bool=True
    # rating:Optional[int]=None

class PostCreate(PostBase):
    pass

class Post(BaseModel):
    title:str
    content: str
    published: bool

    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    email:EmailStr
    password:str
    model_config = ConfigDict(from_attributes=True)

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email:EmailStr
    password:str
