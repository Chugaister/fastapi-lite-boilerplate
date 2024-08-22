from os import getenv
from dotenv import load_dotenv


class EnvVariableNotFound(Exception):
    pass


class Config:

    def __init__(self):
        load_dotenv()
        self.POSTGRES_USER = self.get_var("POSTGRES_USER")
        self.POSTGRES_PASSWORD = self.get_var("POSTGRES_PASSWORD")
        self.POSTGRES_HOST = self.get_var("POSTGRES_HOST")
        self.POSTGRES_DB = self.get_var("POSTGRES_DB")

    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:5432/{self.POSTGRES_DB}"

    @staticmethod
    def get_var(item: str, optional: bool = False):
        var = getenv(item)
        if not var and not optional:
            raise EnvVariableNotFound(f"Environment variable {item} not found")
        return var


config = Config()
