from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import logging

from pricing_model import simulate_dynamic_pricing, generate_market_data
from config import DEBUG

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Retail Pricing Simulator API",
    description="Dynamic pricing platform with ML algorithms for retail optimization",
    version="1.0.0"
)

# Configure CORS to allow the Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://s7f5vd-8000.csb.app"  # For CodeSandbox
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PricingRequest(BaseModel):
    market_intensity: Optional[float] = 50.0
    competition_level: Optional[float] = 0.5
    inventory_level: Optional[float] = 50.0
    seasonal_factor: Optional[float] = 0.0

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global error handler to catch unexpected errors."""
    logger.error(f"Unexpected error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred.", "error": str(exc) if DEBUG else "Internal server error"},
    )

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Retail Pricing Simulator API",
        "version": "1.0.0",
        "endpoints": {
            "/simulate": "POST - Run pricing simulation",
            "/simulate-quick": "GET - Quick simulation with query parameters",
            "/market-data": "GET - Historical market data",
            "/health": "GET - Health check"
        }
    }

@app.post("/simulate")
async def simulate_pricing(request: PricingRequest):
    """
    Run dynamic pricing simulation with detailed parameters.
    """
    try:
        logger.info(f"Running simulation with parameters: {request.dict()}")
        
        input_data = {
            "market_intensity": request.market_intensity,
            "competition_level": request.competition_level,
            "inventory_level": request.inventory_level,
            "seasonal_factor": request.seasonal_factor
        }
        
        result = simulate_dynamic_pricing(input_data)
        logger.info(f"Simulation completed successfully")
        
        return result
        
    except Exception as e:
        logger.error(f"Simulation error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Simulation error: {str(e)}")

@app.get("/simulate-quick")
async def simulate_pricing_quick(
    market_intensity: float = 50.0,
    competition_level: float = 0.5,
    inventory_level: float = 50.0,
    seasonal_factor: float = 0.0
):
    """
    Quick simulation endpoint with query parameters for easy testing.
    """
    try:
        logger.info(f"Running quick simulation with market_intensity: {market_intensity}")
        
        input_data = {
            "market_intensity": market_intensity,
            "competition_level": competition_level,
            "inventory_level": inventory_level,
            "seasonal_factor": seasonal_factor
        }
        
        result = simulate_dynamic_pricing(input_data)
        return result
        
    except Exception as e:
        logger.error(f"Quick simulation error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Simulation error: {str(e)}")

@app.get("/market-data")
async def get_market_data(days: int = 30):
    """
    Get historical market data for visualization.
    """
    try:
        if days < 1 or days > 365:
            raise HTTPException(status_code=400, detail="Days must be between 1 and 365")
        
        logger.info(f"Generating market data for {days} days")
        data = generate_market_data(days)
        
        return {
            "data": data,
            "total_days": len(data),
            "date_range": {
                "start": data[0]["date"] if data else None,
                "end": data[-1]["date"] if data else None
            }
        }
        
    except Exception as e:
        logger.error(f"Market data error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Market data error: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "Retail Pricing Simulator API",
        "timestamp": "2024-01-01T00:00:00Z"
    }

@app.get("/analytics")
async def get_analytics():
    """
    Get real-time analytics and insights.
    """
    try:
        # Generate sample analytics data
        analytics = {
            "total_simulations": 1247,
            "average_price": 98.45,
            "price_trend": "increasing",
            "market_volatility": 0.23,
            "top_strategies": [
                {"strategy": "premium", "usage": 45.2},
                {"strategy": "balanced", "usage": 38.7},
                {"strategy": "competitive", "usage": 16.1}
            ],
            "performance_metrics": {
                "accuracy": 0.87,
                "confidence": 0.92,
                "response_time": "120ms"
            }
        }
        
        return analytics
        
    except Exception as e:
        logger.error(f"Analytics error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Analytics error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    from backend.config import API_HOST, API_PORT
    
    uvicorn.run(
        "backend.main:app",
        host=API_HOST,
        port=API_PORT,
        reload=DEBUG,
        log_level="info"
    )
