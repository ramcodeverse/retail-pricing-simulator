import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import random
from datetime import datetime, timedelta

def simulate_dynamic_pricing(input_features: dict) -> dict:
    """
    Simulate pricing strategies based on input features.
    Uses ML models to generate dynamic pricing recommendations.
    """
    try:
        # Generate realistic historical data for training
        np.random.seed(42)
        n_samples = 1000
        
        # Create features: demand, competition, seasonality, inventory
        demand_factor = np.random.normal(50, 15, n_samples)
        competition_level = np.random.uniform(0.1, 1.0, n_samples)
        seasonality = np.sin(np.linspace(0, 4*np.pi, n_samples)) * 10
        inventory_level = np.random.uniform(10, 100, n_samples)
        
        # Create realistic price based on these factors
        base_price = 100
        prices = (base_price + 
                 demand_factor * 0.8 + 
                 competition_level * -30 + 
                 seasonality + 
                 (100 - inventory_level) * 0.3 + 
                 np.random.normal(0, 5, n_samples))
        
        # Ensure prices are positive
        prices = np.maximum(prices, 20)
        
        # Create training dataset
        training_data = pd.DataFrame({
            'demand': demand_factor,
            'competition': competition_level,
            'seasonality': seasonality,
            'inventory': inventory_level,
            'price': prices
        })
        
        # Train multiple models
        features = ['demand', 'competition', 'seasonality', 'inventory']
        X = training_data[features]
        y = training_data['price']
        
        # Linear Regression Model
        lr_model = LinearRegression()
        lr_model.fit(X, y)
        
        # Random Forest Model
        rf_model = RandomForestRegressor(n_estimators=50, random_state=42)
        rf_model.fit(X, y)
        
        # Extract input parameters
        market_intensity = float(input_features.get("market_intensity", 50))
        competition_level = float(input_features.get("competition_level", 0.5))
        inventory_level = float(input_features.get("inventory_level", 50))
        seasonal_factor = float(input_features.get("seasonal_factor", 0))
        
        # Prepare input for prediction
        input_array = np.array([[market_intensity, competition_level, seasonal_factor, inventory_level]])
        
        # Get predictions from both models
        lr_prediction = lr_model.predict(input_array)[0]
        rf_prediction = rf_model.predict(input_array)[0]
        
        # Average the predictions
        predicted_price = (lr_prediction + rf_prediction) / 2
        predicted_price = max(predicted_price, 10)  # Minimum price floor
        
        # Generate pricing strategy recommendation
        if predicted_price > 120:
            recommendation = "Premium pricing strategy - Market conditions favor higher prices"
            strategy = "premium"
        elif predicted_price < 80:
            recommendation = "Competitive pricing strategy - Lower prices to increase market share"
            strategy = "competitive"
        else:
            recommendation = "Balanced pricing strategy - Maintain current price levels"
            strategy = "balanced"
        
        # Determine market trend
        if competition_level > 0.7:
            market_trend = "Highly competitive"
        elif market_intensity > 70:
            market_trend = "High demand"
        elif inventory_level < 30:
            market_trend = "Low inventory pressure"
        else:
            market_trend = "Stable market conditions"
        
        # Calculate confidence score
        price_variance = abs(lr_prediction - rf_prediction)
        confidence = max(0.6, 1.0 - (price_variance / predicted_price))
        
        # Generate additional insights
        profit_margin = ((predicted_price - 60) / predicted_price) * 100  # Assuming cost of 60
        demand_elasticity = -0.5 + (competition_level * 0.3)  # Simplified elasticity
        
        result = {
            "input_parameters": {
                "market_intensity": market_intensity,
                "competition_level": competition_level,
                "inventory_level": inventory_level,
                "seasonal_factor": seasonal_factor
            },
            "predicted_price": round(predicted_price, 2),
            "recommendation": recommendation,
            "strategy": strategy,
            "market_trend": market_trend,
            "confidence_score": round(confidence, 3),
            "profit_margin": round(profit_margin, 2),
            "demand_elasticity": round(demand_elasticity, 3),
            "model_insights": {
                "linear_regression_price": round(lr_prediction, 2),
                "random_forest_price": round(rf_prediction, 2),
                "price_range": {
                    "min": round(predicted_price * 0.9, 2),
                    "max": round(predicted_price * 1.1, 2)
                }
            },
            "timestamp": datetime.now().isoformat()
        }
        
        return result
        
    except Exception as e:
        raise Exception(f"Pricing simulation error: {str(e)}")

def generate_market_data(days: int = 30) -> list:
    """
    Generate historical market data for visualization
    """
    data = []
    base_date = datetime.now() - timedelta(days=days)
    
    for i in range(days):
        date = base_date + timedelta(days=i)
        
        # Simulate market conditions
        market_intensity = 40 + random.uniform(-10, 20) + (i * 0.5)  # Trending up
        competition = 0.3 + random.uniform(-0.1, 0.4)
        inventory = 60 + random.uniform(-20, 30)
        seasonal = np.sin(i * 0.2) * 5
        
        # Calculate price using similar logic
        price = (100 + market_intensity * 0.6 + competition * -20 + 
                seasonal + (100 - inventory) * 0.2 + random.uniform(-5, 5))
        price = max(price, 30)
        
        data.append({
            "date": date.strftime("%Y-%m-%d"),
            "price": round(price, 2),
            "market_intensity": round(market_intensity, 1),
            "competition_level": round(competition, 2),
            "inventory_level": round(inventory, 1),
            "demand": round(market_intensity + random.uniform(-5, 5), 1)
        })
    
    return data
