from typing import Dict, Any, List, Optional
import os
from fastapi.middleware.cors import CORSMiddleware
import logging

appLogger = logging.getLogger("appLogger")

def configure_cors(app):
    """Configure CORS settings for the FastAPI app."""
    frontend_url = os.environ.get("FRONTEND_URL", "*")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[frontend_url],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

async def handle_exception(request, exc):
    """Global exception handler for unhandled exceptions."""
    appLogger.error(f"Unhandled exception: {exc}")
    return JSONResponse(content={"detail": "Internal Server Error"}, status_code=500)

def setup_middleware(app):
    """Attach middleware to the FastAPI app instance."""
    configure_cors(app)
    app.add_exception_handler(Exception, handle_exception)
