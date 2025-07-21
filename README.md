# Retail Pricing Simulator

A data-driven dynamic pricing platform using machine learning algorithms to optimize retail pricing strategies in real-time.

## Features

- **Dynamic Pricing**: Real-time price optimization based on market conditions
- **ML Algorithms**: Advanced machine learning models using scikit-learn
- **Real-time Analytics**: Live dashboard with comprehensive analytics
- **Market Insights**: Deep market analysis with trend identification
- **Interactive Visualizations**: D3.js powered charts and graphs

## Tech Stack

### Frontend
- **React** with **Next.js** 15
- **TypeScript** for type safety
- **Tailwind CSS** for styling
- **shadcn/ui** for UI components
- **D3.js** for data visualizations
- **Recharts** for additional charts

### Backend
- **Python** with **FastAPI**
- **scikit-learn** for machine learning
- **Pandas** for data manipulation
- **PostgreSQL** for data storage (configurable)
- **Uvicorn** as ASGI server

## Installation

### Prerequisites
- Node.js 18+ and npm
- Python 3.8+
- Git

### 1. Clone the Repository
```bash
git clone <repository-url>
cd retail-pricing-simulator
```

### 2. Frontend Setup
```bash
# Install Node.js dependencies
npm install

# Start the Next.js development server
npm run dev
```

The frontend will be available at `http://localhost:8000`

### 3. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Start the FastAPI server
python start.py
```

The backend API will be available at `http://localhost:5000`

## Usage

### 1. Access the Application
- Open your browser and go to `http://localhost:8000`
- Click "Launch Simulator" to access the main dashboard

### 2. Simulation Parameters
Adjust the following parameters to see different pricing recommendations:

- **Market Intensity** (0-100): Market demand strength
- **Competition Level** (0-1): Level of market competition
- **Inventory Level** (0-100): Current stock levels
- **Seasonal Factor** (-10 to +10): Seasonal demand adjustment

### 3. View Results
The simulator provides:
- **Predicted Price**: AI-generated optimal price
- **Strategy Recommendation**: Premium, Balanced, or Competitive
- **Confidence Score**: Model prediction confidence
- **Profit Margin**: Expected profit percentage
- **Interactive Charts**: Price trends and market analysis

### 4. Real-time Updates
- Enable auto-refresh for real-time price updates
- View historical market data and trends
- Monitor analytics and performance metrics

## API Endpoints

### Main Endpoints
- `GET /` - API information
- `GET /simulate-quick` - Quick simulation with query parameters
- `POST /simulate` - Detailed simulation with JSON payload
- `GET /market-data` - Historical market data
- `GET /analytics` - Real-time analytics
- `GET /health` - Health check

### Example API Usage
```bash
# Quick simulation
curl "http://localhost:5000/simulate-quick?market_intensity=75&competition_level=0.3"

# Get market data
curl "http://localhost:5000/market-data?days=30"

# Health check
curl "http://localhost:5000/health"
```

## Configuration

### Environment Variables
Create a `.env` file in the backend directory:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/pricing_db
DEBUG=true
API_HOST=0.0.0.0
API_PORT=5000
```

### Database Setup (Optional)
For production use with PostgreSQL:

1. Install PostgreSQL
2. Create a database named `pricing_db`
3. Update the `DATABASE_URL` in your environment variables
4. The application will automatically handle database connections

## Development

### Project Structure
```
retail-pricing-simulator/
├── backend/                 # Python FastAPI backend
│   ├── main.py             # FastAPI application
│   ├── pricing_model.py    # ML models and algorithms
│   ├── config.py           # Configuration settings
│   ├── db.py              # Database connection
│   ├── requirements.txt    # Python dependencies
│   └── start.py           # Server startup script
├── src/
│   ├── app/               # Next.js app directory
│   │   ├── layout.tsx     # Root layout
│   │   ├── page.tsx       # Home page
│   │   └── simulator/     # Simulator page
│   └── components/        # React components
│       └── DynamicChart.tsx # D3.js charts
├── public/                # Static assets
└── package.json          # Node.js dependencies
```

### Adding New Features

#### Backend (Python)
1. Add new endpoints in `backend/main.py`
2. Implement ML models in `backend/pricing_model.py`
3. Update configuration in `backend/config.py`

#### Frontend (React/Next.js)
1. Create new pages in `src/app/`
2. Add components in `src/components/`
3. Use shadcn/ui components for consistency

## Machine Learning Models

The simulator uses multiple ML approaches:

1. **Linear Regression**: For baseline price predictions
2. **Random Forest**: For complex pattern recognition
3. **Ensemble Method**: Combines multiple models for accuracy

### Model Features
- Market intensity and demand patterns
- Competition level analysis
- Inventory pressure factors
- Seasonal demand adjustments

## Troubleshooting

### Common Issues

1. **Backend not starting**
   - Check if Python dependencies are installed: `pip install -r backend/requirements.txt`
   - Verify Python version is 3.8+
   - Check if port 5000 is available

2. **Frontend build errors**
   - Clear node_modules: `rm -rf node_modules && npm install`
   - Check Node.js version is 18+
   - Try using `--legacy-peer-deps` flag

3. **API connection errors**
   - Ensure backend is running on port 5000
   - Check CORS settings in `backend/main.py`
   - Verify API_BASE_URL in frontend code

4. **Chart rendering issues**
   - Check browser console for D3.js errors
   - Ensure data is properly formatted
   - Verify SVG dimensions and scales

## Performance Optimization

### Backend
- Use async/await for database operations
- Implement caching for frequently accessed data
- Add request rate limiting for production

### Frontend
- Implement React.memo for expensive components
- Use Next.js Image optimization
- Add loading states and error boundaries

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with detailed description

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Check the troubleshooting section above
- Review API documentation at `http://localhost:5000/docs`
- Create an issue in the repository

---

**Coded by Ram Codeverse**  
Built with modern web technologies for optimal performance and user experience.
