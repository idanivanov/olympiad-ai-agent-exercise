"""Settings for the AI Agents Exercise."""

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    """Settings for the AI Agents Exercise."""

    model_config = SettingsConfigDict(env_file=".env")

    OPENAI_API_KEY: str

    LANGCHAIN_API_KEY: str
    LANGCHAIN_TRACING_V2: bool = True
    LANGCHAIN_ENDPOINT: str = "https://api.smith.langchain.com"
    LANGCHAIN_PROJECT: str = "su-olympiad-lecture"
