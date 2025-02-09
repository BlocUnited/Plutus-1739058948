from typing import Dict, Any, List, Optional
import os
from fastapi import APIRouter, HTTPException
from backend.models.portfolio import PortfolioModel
from backend.services.portfolio_service import PortfolioService
from pydantic import BaseModel
import logging

router = APIRouter()
logger = logging.getLogger("appLogger")
portfolio_service = PortfolioService()

class CreatePortfolioRequest(BaseModel):
    userId: str
    title: str
    description: str

class GetPortfolioResponse(BaseModel):
    portfolio: PortfolioModel

@router.post("/portfolios", response_model=PortfolioModel)
async def create_portfolio(request: CreatePortfolioRequest):
    """Handle creating a new portfolio."""
    try:
        portfolio = await portfolio_service.create_portfolio(request.userId, request.title, request.description)
        return portfolio
    except Exception as e:
        logger.error(f"Portfolio creation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/portfolios/{portfolioId}", response_model=GetPortfolioResponse)
async def get_portfolio(portfolioId: str):
    """Handle retrieving a portfolio by ID."""
    try:
        portfolio = await portfolio_service.get_portfolio(portfolioId)
        return {"portfolio": portfolio}
    except Exception as e:
        logger.error(f"Portfolio retrieval error: {e}")
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/portfolios/{portfolioId}/like")
async def like_portfolio(portfolioId: str, userId: str):
    """Handle liking a portfolio."""
    try:
        likes_count = await portfolio_service.like_portfolio(portfolioId, userId)
        return {"likes": likes_count}
    except Exception as e:
        logger.error(f"Like portfolio error: {e}")
        raise HTTPException(status_code=404, detail=str(e))
