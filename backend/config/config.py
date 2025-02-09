from typing import Dict, Any, List, Optional
import os

class Config:
    """Configuration class to hold environment variables and settings."""
    DATABASE_URI = os.environ.get('DATABASE_URI')
    if DATABASE_URI is None:
        raise ValueError("DATABASE_URI environment variable is required.")
    BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:5000')
    FRONTEND_URL = os.environ.get('FRONTEND_URL', '*')

    AZURE_SIGNALR_CONNECTION_STRING = os.environ.get('AZURE_SIGNALR_CONNECTION_STRING')
    AZURE_STORAGE_CONNECTION_STRING = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

    @staticmethod
    def log_config():
        import logging
        logger = logging.getLogger("appLogger")
        logger.info(f"Starting application with BACKEND_URL={Config.BACKEND_URL} and FRONTEND_URL={Config.FRONTEND_URL}")
