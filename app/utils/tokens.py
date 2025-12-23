from jose import jwt
from app.core.config import settings
from datetime import datetime,timedelta


def create_access_token(data:dict)->str:
    to_encode=data.copy()
    expire_time=datetime.utcnow()+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire_time})
    return jwt.encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGORITHM)