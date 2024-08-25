from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuration(BaseSettings):
    model_config = SettingsConfigDict(env_file='src/.env', env_file_encoding='utf-8')
    login: str
    base_folder: str


class SMTPSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='smtp_', env_file='src/.env', env_file_encoding='utf-8')
    server: str
    port: int
    email: str
    email_password: str
