import json
from os.path import dirname, join
from fastapi import FastAPI
from gospeed_api.index import GospeedAPI
from v1.models.settings import Settings

app = FastAPI()

settings_file = join(dirname(__file__), 'civitai_browser_settings.json')
sqlite_file = join(dirname(__file__), 'db.sqlite3')

with open(settings_file, 'r') as f:
    data = json.load(f)
    settings = Settings(**data)

gospeed_api = GospeedAPI(gopeed_host=settings.gopeed_url)