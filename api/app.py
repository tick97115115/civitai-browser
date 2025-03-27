from os.path import dirname, join
from fastapi import FastAPI
from gospeed_api.index import GospeedAPI

app = FastAPI()

settings_file = join(dirname(__file__), 'civitai_browser_settings.json')
sqlite_file = join(dirname(__file__), 'db.sqlite3')
