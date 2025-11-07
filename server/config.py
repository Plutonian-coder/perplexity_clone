from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    TAVILY_API_KEY: str = "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"
    GEMINI_API_KEY: str = "AIzaSyDKG_J-TMbaQ42C2GJVJxLmtQHlrF_ssqc"


