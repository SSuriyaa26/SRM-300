from jose import jwt,JWTError
from datetime import datetime,timedelta
from . import schemas
SECRET_KEY = "hello"# this ideally stores ur secret key , using hello as an example
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

def create_access_token(data:dict):
    to_encode=data.copy()

    expire=datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token:str,credentials_exception):
    payload =jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)

    id:str = payload.get("users_id")
    if id is None:
        raise credentials_exception