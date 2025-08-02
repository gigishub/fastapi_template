from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    # Application
    app_name: str = "FastAPI Template"
    debug: bool = True
    version: str = "1.0.0"
    
    # Security
    secret_key: str = "your-secret-key-change-this-in-production"
    access_token_expire_minutes: int = 30
    
    # API
    api_v1_prefix: str = "/api/v1"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

class Endpoints:
    """
    API endpoint constants.
    """
    API_V1_PREFIX = "/api/v1"
    REGISTER = "/register"
    LOGIN = "/login"
    LOGOUT = "/logout"
    USERS = "/users"

# Global settings instance
settings = Settings()
