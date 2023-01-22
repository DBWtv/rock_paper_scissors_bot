from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database:    str  # name of database
    db_host:     str  # database url
    db_user:     str  # username of DB user
    db_password: str  # password of DB user


@dataclass
class TgBot:
    token: str  # access token
    admin_ids: list[int]  # list of admin ids


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str or None) -> Config:

    env: Env = Env()
    env.read_env()

    return Config(tg_bot=TgBot(token=env('TOKEN'),
                             admin_ids=list(map(int, env.list('ADMIN_IDS')))),
                db=DatabaseConfig(database=env('DATABASE'),
                                  db_host=env('DB_HOST'),
                                  db_user=env('DB_USER'),
                                  db_password=env('DB_PASSWORD')))