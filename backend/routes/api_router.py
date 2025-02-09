from typing import Dict, Any, List, Optional
import os
from fastapi import APIRouter
from backend.controllers.user_controller import router as user_router
from backend.controllers.portfolio_controller import router as portfolio_router
from backend.controllers.community_controller import router as community_router
from backend.controllers.ai_mentor_controller import router as ai_mentor_router

api_router = APIRouter(prefix='/api')

# Include user routes
api_router.include_router(user_router)

# Include portfolio routes
api_router.include_router(portfolio_router)

# Include community routes
api_router.include_router(community_router)

# Include AI mentor routes
api_router.include_router(ai_mentor_router)
