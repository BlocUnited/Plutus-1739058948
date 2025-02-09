from typing import Dict, Any, List, Optional
import os
from pydantic import BaseModel, Field, EmailStr, validator
from bson import ObjectId
from typing import Optional, List
import logging

logger = logging.getLogger("appLogger")

class UserModel(BaseModel):
    """Model representing a user in the application."""
    id: str = Field(default_factory=lambda: str(ObjectId()), alias='_id')
    username: str = Field(..., max_length=50)
    email: EmailStr
    passwordHash: str
    profile: dict
    socialLinks: dict
    portfolio: List[str] = []
    achievements: List[str] = []
    role: str = Field(default="user")
    createdAt: str
    updatedAt: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

    @validator('username')
    def validate_username(cls, v):
        if not v:
            logger.error("Username must not be empty.")
            raise ValueError("Username must not be empty.")
        return v

    @validator('email')
    def validate_email(cls, v):
        if not v:
            logger.error("Email must not be empty.")
            raise ValueError("Email must not be empty.")
        return v
