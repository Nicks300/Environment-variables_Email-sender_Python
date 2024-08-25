from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuration(BaseSettings):
    model_config = SettingsConfigDict(env_file='src/.env',
                                      env_file_encoding='utf-8')  # может потребоваться env_file = '.env'
    login: str
    base_folder: str
