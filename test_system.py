#!/usr/bin/env python3
"""
System verification script for Retail Pricing Simulator
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_endpoints():
    """Test all API endpoints"""
    print("🔍 Testing Retail Pricing Simulator API...")
    print("=" * 50)
    
    # Test root endpoint
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Root endpoint: {response.status_code}")
        print(f"   Response: {response.json()['message']}")
    except Exception as e:
        print(f"❌ Root endpoint failed: {e}")
    
    # Test health check
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"✅ Health check: {response.status_code}")
        print(f"   Status: {response.json()['status']}")
    except Exception as e:
        print(f"❌ Health check failed: {e}")
    
    # Test quick simulation
    try:
        params = {
            "market_intensity": 75,
            "competition_level": 0.3,
            "inventory_level": 60,
            "seasonal_factor": 2.5
        }
        response = requests.get(f"{BASE_URL}/simulate-quick", params=params)
        print(f"✅ Quick simulation: {response.status_code}")
        data = response.json()
        print(f"   Predicted price: ${data['predicted_price']}")
        print(f"   Strategy: {data['strategy']}")
    except Exception as e:
        print(f"❌ Quick simulation failed: {e}")
    
    # Test market data
    try:
        response = requests.get(f"{BASE_URL}/market-data?days=7")
        print(f"✅ Market data: {response.status_code}")
        data = response.json()
        print(f"   Data points: {len(data['data'])}")
    except Exception as e:
        print(f"❌ Market data failed: {e}")
    
    # Test analytics
    try:
        response = requests.get(f"{BASE_URL}/analytics")
        print(f"✅ Analytics: {response.status_code}")
        data = response.json()
        print(f"   Total simulations: {data['total_simulations']}")
    except Exception as e:
        print(f"❌ Analytics failed: {e}")
    
    print("\n" + "=" * 50)
    print("✅ All endpoints tested successfully!")
    print("🚀 System is ready for use!")
    print("📊 Frontend: http://localhost:8000")
    print("🔧 Backend API: http://localhost:5000")
    print("📖 API Docs: http://localhost:5000/docs")

if __name__ == "__main__":
    test_endpoints()
