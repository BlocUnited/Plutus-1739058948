from typing import Dict, Any, List, Optional
import os
import logging
from fastapi import FastAPI
from backend.config.config import Config
from backend.database.database import get_database
from backend.middleware.middleware import setup_middleware
from backend.routes.api_router import api_router

# Initialize logging
logging.basicConfig(level=logging.INFO)
appLogger = logging.getLogger("appLogger")

# Load global configuration
Config.log_config()

# Create FastAPI app instance
app = FastAPI()

# Setup middleware
setup_middleware(app)

# Register routes
app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    """Event handler for application startup."""
    await get_database()  # Ensure database connection is established
    appLogger.info("Database connection established.")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
