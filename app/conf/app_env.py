import os
from pathlib import Path

from dotenv import load_dotenv


class UserEnv:
    def __init__(self):
        self.__load_user_env()

    @staticmethod
    def __load_user_env():
        try:
            env_path = Path(".") / ".env"
            load_dotenv(dotenv_path=env_path)
        except IOError as e:
            print({"error": f"File not found! - {e}"})
        except Exception as e:
            print({"error": f"File not found! - {e}"})

    @staticmethod
    def get_env_value(key: str) -> str:
        return os.getenv(key)
