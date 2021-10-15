import json
from dataclasses import dataclass


@dataclass
class Bot:
    token: str


@dataclass
class DB:
    host: str
    db_name: str
    user: str
    password: str


@dataclass
class Config:
    bot: Bot
    db: DB


def get_settings(k):
    with open('settings.json', 'r', encoding='utf-8') as f:
        return json.loads(f.read()).get(k)


def load_config():
    # TODO: Add some checks here?
    return Config(
        bot=Bot(token=get_settings("BOT_TOKEN")),
        db=DB(
            host=get_settings("DB_HOST"),
            db_name=get_settings("DB_NAME"),
            user=get_settings("DB_USER"),
            password=get_settings("DB_PASS")
        )
    )
