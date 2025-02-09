from typing import Dict, Any, List, Optional
import os
from fastapi import APIRouter, HTTPException
from backend.models.community import CommunityModel
from backend.services.community_service import CommunityService
from pydantic import BaseModel
import logging

router = APIRouter()
logger = logging.getLogger("appLogger")
community_service = CommunityService()

class CreateCommunityRequest(BaseModel):
    name: str
    description: str

@router.post("/communities", response_model=CommunityModel)
async def create_community(request: CreateCommunityRequest):
    """Handle creating a new community."""
    try:
        community = await community_service.create_community(request.name, request.description)
        return community
    except Exception as e:
        logger.error(f"Community creation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/communities/{communityId}/join")
async def join_community(userId: str, communityId: str):
    """Handle joining a community."""
    try:
        updated_community = await community_service.join_community(userId, communityId)
        return updated_community
    except Exception as e:
        logger.error(f"Join community error: {e}")
        raise HTTPException(status_code=404, detail=str(e))
