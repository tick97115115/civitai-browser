from sqlmodel import create_engine, SQLModel
from api.v1.routers.settings import init, load_settings
settings = init()

from api.app import app
from api.v1.routers.settings import router as settings_router
from api.v1.routers.ai_models import router as download_router
import api.v1.db.civitai_table
import api.v1.db.gopeed_table
app.include_router(settings_router)
app.include_router(download_router)

settings = load_settings()
engine = create_engine(settings.db_uri)
SQLModel.metadata.create_all(engine)

# if __name__ == '__main__':
#     settings = init()
#     app.include_router(settings_router)    