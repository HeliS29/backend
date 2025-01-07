from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:root@127.0.0.1:3306/activate"
    JWT_SECRET: str = "your_jwt_secret_key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
