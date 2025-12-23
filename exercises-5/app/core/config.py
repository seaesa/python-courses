from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    TZ: str = "Asia/Ho_Chi_Minh"
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20

    class Config:
        env_file = ".env"


settings = Settings()
