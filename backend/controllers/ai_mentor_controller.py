from typing import Dict, Any, List, Optional
import os
from fastapi import APIRouter, HTTPException
from backend.services.ai_mentor_service import AIMentorService
from pydantic import BaseModel
import logging

router = APIRouter()
logger = logging.getLogger("appLogger")
ai_mentor_service = AIMentorService()

class GenerateAIResponseRequest(BaseModel):
    userId: str
    prompt: str

@router.post("/ai/mentor")
async def generate_ai_response(request: GenerateAIResponseRequest):
    """Handle generating an AI response."""
    try:
        response = await ai_mentor_service.generate_ai_response(request.userId, request.prompt)
        return {"response": response}
    except Exception as e:
        logger.error(f"AI response generation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
