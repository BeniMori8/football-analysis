from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator


class Config(BaseSettings):
    # הגדרות הלוגר
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    # הגדרות עיבוד
    chunk_size: int = Field(default=10000, alias="CHUNK_SIZE")
    yellow_card_threshold: int = Field(default=5, alias="YELLOW_CARD_THRESHOLD")

    # נתיבים
    data_path: str = Field(default="data/league_matches.csv", alias="DATA_PATH")
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @field_validator('log_level')
    @classmethod
    def validate_score(cls, value):
        valid_values = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if value not in valid_values:
            raise ValueError('level is not exist!')
        return value

config = Config()