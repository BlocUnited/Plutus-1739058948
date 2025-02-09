from typing import Dict, Any, List, Optional
import os
from backend.models.community import CommunityModel
from backend.database.database import get_database
import logging

logger = logging.getLogger("appLogger")

class CommunityService:
    """Service class for community-related operations."""

    async def create_community(self, name: str, description: str) -> CommunityModel:
        """Create a new community and return the community model."""
        db = await get_database()
        community = CommunityModel(
            name=name,
            description=description,
            members=[],
            posts=[],
            createdAt=datetime.utcnow().isoformat()
        )
        try:
            await db["Communities"].insert_one(community.dict(by_alias=True))
            logger.info(f"Community created: {name}")
            return community
        except Exception as e:
            logger.error(f"Error creating community: {e}")
            raise HTTPException(status_code=400, detail="Community creation failed.")

    async def join_community(self, userId: str, communityId: str) -> CommunityModel:
        """Join a community and return the updated community model."""
        db = await get_database()
        updated_community = await db["Communities"].find_one_and_update(
            {"_id": ObjectId(communityId)},
            {"$addToSet": {"members": userId}}
        )
        if updated_community:
            logger.info(f"User {userId} joined community: {communityId}")
            return CommunityModel(**updated_community)
        logger.warning(f"Community not found for join: {communityId}")
        raise HTTPException(status_code=404, detail="Community not found")
