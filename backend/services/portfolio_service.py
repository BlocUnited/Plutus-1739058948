from typing import Dict, Any, List, Optional
import os
from backend.models.portfolio import PortfolioModel
from backend.database.database import get_database
import logging

logger = logging.getLogger("appLogger")

class PortfolioService:
    """Service class for portfolio-related operations."""

    async def create_portfolio(self, userId: str, title: str, description: str) -> PortfolioModel:
        """Create a new portfolio and return the portfolio model."""
        db = await get_database()
        portfolio = PortfolioModel(
            userId=userId,
            title=title,
            description=description,
            media=[],
            tags=[],
            likes=0,
            comments=[],
            createdAt=datetime.utcnow().isoformat()
        )
        try:
            await db["Portfolios"].insert_one(portfolio.dict(by_alias=True))
            logger.info(f"Portfolio created: {title}")
            return portfolio
        except Exception as e:
            logger.error(f"Error creating portfolio: {e}")
            raise HTTPException(status_code=400, detail="Portfolio creation failed.")

    async def get_portfolio(self, portfolioId: str) -> PortfolioModel:
        """Get a portfolio by ID."""
        db = await get_database()
        portfolio = await db["Portfolios"].find_one({"_id": ObjectId(portfolioId)})
        if portfolio:
            logger.info(f"Portfolio retrieved: {portfolioId}")
            return PortfolioModel(**portfolio)
        logger.warning(f"Portfolio not found: {portfolioId}")
        raise HTTPException(status_code=404, detail="Portfolio not found")

    async def like_portfolio(self, portfolioId: str, userId: str) -> int:
        """Like a portfolio and return the updated like count."""
        db = await get_database()
        result = await db["Portfolios"].find_one_and_update(
            {"_id": ObjectId(portfolioId)},
            {"$inc": {"likes": 1}}
        )
        if result:
            logger.info(f"Portfolio liked: {portfolioId}")
            return result["likes"] + 1
        logger.warning(f"Portfolio not found for like: {portfolioId}")
        raise HTTPException(status_code=404, detail="Portfolio not found")
