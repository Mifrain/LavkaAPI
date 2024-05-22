from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URI: str
    
    
    model_config =  BaseSettings(env_file=".env")
    
    
settings = Settings()
        