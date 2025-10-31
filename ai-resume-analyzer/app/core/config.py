# ai-resume-analyzer/app/core/config.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    """Configuration settings for the application."""
    
    # Application settings
    app_name: str = "AI Resume Analyzer"
    app_version: str = "1.0.0"
    
    # Database settings
    database_url: str
    
    # Other settings can be added here
    # For example, you might want to add settings for logging, API keys, etc.

    class Config:
        """Pydantic configuration."""
        env_file = ".env"  # Load environment variables from .env file

settings = Settings()  # Instantiate the settings object for use throughout the application