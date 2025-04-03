from fastapi import APIRouter, Request, FastAPI
from fastapi.responses import JSONResponse
from pydantic_settings import BaseSettings
from pydantic import Field
import httpx
from os.path import join, dirname, exists
import json
from urllib.parse import urljoin
from os.path import dirname, join
from gospeed_api.index import GospeedAPI
from civitai_api.v1 import CiviClient

app = FastAPI()

settings_file = join(dirname(__file__), 'civitai_browser_settings.json')
sqlite_file = join(dirname(__file__), 'db.sqlite3')

class Settings(BaseSettings):
    db_uri: str = Field(default='sqlite:///' + sqlite_file)
    lora_folder: str = ''
    checkpoint_folder: str = ''
    proxy: str = ''
    api_key: str = ''
    gopeed_url: str = ''

router = APIRouter()

# https://fastapi.tiangolo.com/tutorial/handling-errors/?h=exce#install-custom-exception-handlers

class LoadSettingsError(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg

@app.exception_handler(LoadSettingsError)
async def load_settings_exception_handler(request: Request, exc: LoadSettingsError):
    return JSONResponse(
        status_code=500,
        content={"message": exc.msg},
    )

class DatabaseNotFound(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg

@app.exception_handler(DatabaseNotFound)
async def database_not_found_exception_handler(request: Request, exc: DatabaseNotFound):
    return JSONResponse(
        status_code=500,
        content={"message": exc.msg},
    )

class LoraFolderNotFound(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg

@app.exception_handler(LoraFolderNotFound)
async def lora_folder_not_found_exception_handler(request: Request, exc: LoraFolderNotFound):
    return JSONResponse(
        status_code=500,
        content={"message": exc.msg},
    )

class CheckpointFolderNotFound(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg

@app.exception_handler(CheckpointFolderNotFound)
async def checkpoint_folder_not_found_exception_handler(request: Request, exc: CheckpointFolderNotFound):
    return JSONResponse(
        status_code=500,
        content={"message": exc.msg},
    )

class GopeedServiceNotFound(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg
    
@app.exception_handler(GopeedServiceNotFound)
async def gopeed_service_not_found_exception_handler(request: Request, exc: GopeedServiceNotFound):
    return JSONResponse(
        status_code=500,
        content={"message": exc.msg},
    )

class GopeedServiceNotWorking(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg

@app.exception_handler(GopeedServiceNotWorking)
async def gopeed_service_not_working_exception_handler(request: Request, exc: GopeedServiceNotWorking):
    return JSONResponse(
        status_code=500,
        content={"message": exc.msg},
    )

def check_settings(settings: Settings):
    # check if lora_folder exists
    if not exists(settings.lora_folder):
        raise LoraFolderNotFound(msg="lora folder doesn't exists")
    
    # check if checkpoint_folder exists
    if not exists(settings.checkpoint_folder):
        raise CheckpointFolderNotFound(msg="checkpoint folder doesn't exists")
    
    # check if gopeed_url exists
    if not settings.gopeed_url:
        raise GopeedServiceNotFound(msg="gopeed service url not found")
    
    # check if gopeed service is working
    response = httpx.get(urljoin(settings.gopeed_url, '/api/v1/info'))
    if response.status_code != 200:
        raise GopeedServiceNotWorking(msg="gopeed service not working")
    
    # check database
    # if not exists(settings.db_uri):
    #     raise DatabaseNotFound(msg="database doesn't exists")

@router.get("/api/v1/settings", response_model=Settings)
def load_settings() -> Settings:
    # if file content broken makes it un deserializable
    try:
        with open(settings_file, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            # if settings option value (like lora_folder) can't be found
            settings = Settings(**data)
            check_settings(settings)
            return settings
    except Exception as e:
        raise LoadSettingsError(str(e))

@router.post("/api/v1/settings")
def save_settings(settings: Settings):
    with open(settings_file, 'w', encoding="utf-8") as f:
        f.write(settings.model_dump_json(indent=2))

def init() -> Settings:
    initial_check_pass: bool = False
    settings: Settings

    while not initial_check_pass:
        # check if settings file exists
        if not exists(settings_file):
            print("settings file not found, creating new one.")
            settings = Settings()
            save_settings(settings)
            continue

        # check if settings are correct
        try:
            settings = load_settings()
            check_settings(settings)
        except LoadSettingsError:
            settings = Settings()
            save_settings(settings)
            print("Load settings.json failed, replace \".settings.json\" with default values.")
            input(f"Please edit \"{settings_file}\", then Press enter to continue...")
            continue
        except LoraFolderNotFound:
            print("Lora folder not found")
            input("please check \"lora_folder\" value in \".settings.json\" then Press enter to continue...")
            continue
        except CheckpointFolderNotFound:
            print("Checkpoint folder not found")
            input("please check \"checkpoint_folder\" value in \".settings.json\" then Press enter to continue...")
            continue
        except GopeedServiceNotWorking:
            print("Gopeed service not working")
            input("please check \"gopeed_url\" value in \".settings.json\" then Press enter to continue...")
            continue
        # except DatabaseNotFound:
        #     print("Database not found, is this your first time running the app?")
        #     answer = input("(Y/N): ")
        #     if answer.lower() == 'y':
        #         print("Creating new database...")
        #         from sqlmodel import create_engine, SQLModel, Session
        #         SQLModel.metadata.create_all(engine)
        #     else:
        #         print("Please check \"db_uri\" value in \".settings.json\"")
        #         input("Press enter to continue...")
        #     continue

        initial_check_pass = True
    
    return settings

settings = init()

gospeed_api = GospeedAPI(gopeed_host=settings.gopeed_url)

def instantiate_civitai_client(settings: Settings):
    if settings.proxy != '':
        httpx_client = httpx.Client(proxy=settings.proxy)
        async_httpx_client = httpx.AsyncClient(proxy=settings.proxy)
        return CiviClient(settings.api_key, httpx_client, async_httpx_client)
    else:
        return CiviClient(settings.api_key)

civitai_api = instantiate_civitai_client(settings)
