from typing import Dict, Any, List, Optional
import os
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import List, Optional
import logging

logger = logging.getLogger("appLogger")

class PortfolioModel(BaseModel):
    """Model representing a portfolio in the application."""
    id: str = Field(default_factory=lambda: str(ObjectId()), alias='_id')
    userId: str
    title: str = Field(..., max_length=100)
    description: Optional[str] = None
    media: List[dict] = []
    tags: List[str] = []
    likes: int = 0
    comments: List[str] = []
    createdAt: str

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
