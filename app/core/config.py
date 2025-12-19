from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    APP_NAME:str="Hospital Platform"
    ENV:str="devlopment"
    DEBUG:bool=False

    SECRET_KEY:str=Field(...,min_length=32)
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 15
    REFRESH_TOKEN_EXPIRE_DAYS:int=7
    ALGORITHM:str="HS256"

    DATABASE_URL:str 


    ALLOWED_ORIGINS: list[str] = ["*"]


    class Config:
        env_file=".env"
        extra="ignore"

settings =Settings()