from typing import Dict, Any, List, Optional
import os
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import List, Optional
import logging

logger = logging.getLogger("appLogger")

class CommunityModel(BaseModel):
    """Model representing a community in the application."""
    id: str = Field(default_factory=lambda: str(ObjectId()), alias='_id')
    name: str = Field(..., max_length=100)
    description: Optional[str] = None
    members: List[dict] = []
    posts: List[str] = []
    createdAt: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

    @validator('name')
    def validate_name(cls, v):
        if not v:
            logger.error("Community name must not be empty.")
            raise ValueError("Community name must not be empty.")
        return v
