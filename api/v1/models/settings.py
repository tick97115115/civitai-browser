from pydantic import BaseSettings, Field
class Settings(BaseSettings):
    db_uri: str = Field(default='sqlite:///' + sqlite_file)
    lora_folder: str = ""
    checkpoint_folder: str = ''
    proxy: str | None = Field(default=None)
    api_key: str | None = Field(default=None)
    gopeed_url: str | None = Field(default=None)