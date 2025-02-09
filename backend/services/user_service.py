from typing import Dict, Any, List, Optional
import os
import bcrypt
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from backend.models.user import UserModel
from backend.database.database import get_database
import logging

logger = logging.getLogger("appLogger")

class UserService:
    """Service class for user-related operations."""

    async def register_user(self, email: str, username: str, password: str) -> UserModel:
        """Register a new user and return the user model."""
        db = await get_database()
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = UserModel(
            username=username,
            email=email,
            passwordHash=hashed_password,
            profile={"displayName": username, "bio": "", "profileImageUrl": "", "skills": [], "interests": []},
            socialLinks={},
            portfolio=[],
            achievements=[],
            role="user",
            createdAt=datetime.utcnow().isoformat(),
            updatedAt=datetime.utcnow().isoformat()
        )
        try:
            await db["Users"].insert_one(user.dict(by_alias=True))
            logger.info(f"User registered: {username}")
            return user
        except Exception as e:
            logger.error(f"Error registering user: {e}")
            raise HTTPException(status_code=400, detail="User registration failed.")

    async def login_user(self, email: str, password: str) -> str:
        """Login a user and return a JWT token."""
        db = await get_database()
        user = await db["Users"].find_one({"email": email})
        if user and bcrypt.checkpw(password.encode(), user["passwordHash"].encode()):
            token = jwt.encode({"sub": str(user["_id"]), "exp": datetime.utcnow() + timedelta(hours=1)}, "SECRET_KEY", algorithm="HS256")
            logger.info(f"User logged in: {user['username']}")
            return token
        logger.warning(f"Login failed for email: {email}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    async def update_profile(self, userId: str, profileData: dict) -> UserModel:
        """Update user profile and return the updated user model."""
        db = await get_database()
        updated_user = await db["Users"].find_one_and_update(
            {"_id": ObjectId(userId)},
            {"$set": {"profile": profileData, "updatedAt": datetime.utcnow().isoformat()}}
        )
        if updated_user:
            logger.info(f"User profile updated: {userId}")
            return UserModel(**updated_user)
        logger.warning(f"User not found for update: {userId}")
        raise HTTPException(status_code=404, detail="User not found")
