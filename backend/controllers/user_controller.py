from typing import Dict, Any, List, Optional
import os
from fastapi import APIRouter, HTTPException, Depends
from backend.models.user import UserModel
from backend.services.user_service import UserService
from pydantic import BaseModel
import logging

router = APIRouter()
logger = logging.getLogger("appLogger")
user_service = UserService()

class RegisterUserRequest(BaseModel):
    email: str
    username: str
    password: str

class LoginUserRequest(BaseModel):
    email: str
    password: str

class UpdateProfileRequest(BaseModel):
    profile: dict

@router.post("/users/register", response_model=UserModel)
async def register_user(request: RegisterUserRequest):
    """Handle user registration."""
    try:
        user = await user_service.register_user(request.email, request.username, request.password)
        return user
    except Exception as e:
        logger.error(f"Registration error: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/users/login")
async def login_user(request: LoginUserRequest):
    """Handle user login."""
    try:
        token = await user_service.login_user(request.email, request.password)
        return {"access_token": token}
    except Exception as e:
        logger.error(f"Login error: {e}")
        raise HTTPException(status_code=401, detail=str(e))

@router.put("/users/profile", response_model=UserModel)
async def update_user_profile(userId: str, request: UpdateProfileRequest):
    """Handle updating user profile."""
    try:
        updated_user = await user_service.update_profile(userId, request.profile)
        return updated_user
    except Exception as e:
        logger.error(f"Profile update error: {e}")
        raise HTTPException(status_code=404, detail=str(e))
