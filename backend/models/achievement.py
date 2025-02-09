from typing import Dict, Any, List, Optional
import os
from pydantic import BaseModel, Field
from bson import ObjectId
import logging

logger = logging.getLogger("appLogger")

class AchievementModel(BaseModel):
    """Model representing an achievement in the application."""
    id: str = Field(default_factory=lambda: str(ObjectId()), alias='_id')
    userId: str
    title: str
    description: Optional[str] = None
    points: int = 0
    earnedAt: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

    @validator('title')
    def validate_title(cls, v):
        if not v:
            logger.error("Title must not be empty.")
            raise ValueError("Title must not be empty.")
        return v
