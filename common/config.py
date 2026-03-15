import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("BASE_URL", "")
    USERNAME = os.getenv("USERNAME", "")
    PASSWORD = os.getenv("PASSWORD", "")
    TOKEN = os.getenv("TOKEN", "")
    OWNER = os.getenv("OWNER", "")
    PUBLIC_USER = os.getenv("PUBLIC_USER", "")
    REPO_NAME_BASE = os.getenv("REPO_NAME_BASE", "")
    REPO_NAME_TEMP = os.getenv("REPO_NAME_TEMP", "")
    PRIVATE_REPO_NAME = os.getenv("PRIVATE_REPO_NAME", "")
    COLLABORATOR = os.getenv("COLLABORATOR", "")

    MYSQL_HOST = os.getenv("MYSQL_HOST", "")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER = os.getenv("MYSQL_USER", "")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DB = os.getenv("MYSQL_DB", "")

    @classmethod
    def auth_headers(cls) -> dict:
        return {
            "Authorization": f"token {cls.TOKEN}",
            "Content-Type": "application/json",
        }

