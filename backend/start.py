#!/usr/bin/env python3
"""
Startup script for the Retail Pricing Simulator API
"""

import sys
import os
import subprocess
import time

def check_dependencies():
    """Check if required Python packages are installed"""
    try:
        import fastapi
        import uvicorn
        import pandas
        import sklearn
        import numpy
        print("✓ All required dependencies are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("Please install dependencies with: pip install -r requirements.txt")
        return False

def start_server():
    """Start the FastAPI server"""
    try:
        print("Starting Retail Pricing Simulator API...")
        print("Server will be available at: http://localhost:5000")
        print("API documentation at: http://localhost:5000/docs")
        print("Press Ctrl+C to stop the server")
        print("-" * 50)
        
        # Start the server
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--host", "0.0.0.0", 
            "--port", "5000", 
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\n\nServer stopped by user")
    except Exception as e:
        print(f"Error starting server: {e}")

if __name__ == "__main__":
    print("Retail Pricing Simulator - Backend Server")
    print("=" * 50)
    
    if check_dependencies():
        start_server()
    else:
        sys.exit(1)
