import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7416997325:AAEBcJhyCarX22KewNFHA4ktzTrAiA9DQaM")

    APP_ID = int(os.environ.get("APP_ID", 26701855))

    API_HASH = os.environ.get("API_HASH", "cd5b268d89348d68b451310653274f4c")
