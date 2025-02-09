from typing import Dict, Any, List, Optional
import os
from pydantic import BaseModel, Field
from bson import ObjectId
import logging

logger = logging.getLogger("appLogger")

class AIMentorModel(BaseModel):
    """Model representing an AI mentor interaction."""
    id: str = Field(default_factory=lambda: str(ObjectId()), alias='_id')
    userId: str
    prompt: str
    response: str
    createdAt: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

    @validator('prompt')
    def validate_prompt(cls, v):
        if not v:
            logger.error("Prompt must not be empty.")
            raise ValueError("Prompt must not be empty.")
        return v
