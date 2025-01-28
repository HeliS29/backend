from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:Root1234!@127.0.0.1:3306/activate"
    JWT_SECRET: str = "your_jwt_secret_key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
# from pydantic_settings import BaseSettings
# from dotenv import load_dotenv
# load_dotenv()
# import os

# # DB_URI = f"{os.getenv('DB_ENG')}{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/"
# class Settings(BaseSettings):
#     DATABASE_URL: str = ""
#     JWT_SECRET: str = os.getenv('JWT_SECRET', 'your_jwt_secret_key')
#     JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM', 'HS256')
#     JWT_EXPIRATION_MINUTES: int = int(os.getenv('JWT_EXPIRATION_MINUTES', 30))

#     class Config:
#         env_file = ".env"

# settings = Settings()
