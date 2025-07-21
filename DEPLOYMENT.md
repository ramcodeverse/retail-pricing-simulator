# GitHub Deployment Guide

## 🚀 Quick GitHub Setup

### 1. Create GitHub Repository
```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit: Retail Pricing Simulator"

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/retail-pricing-simulator.git
git branch -M main
git push -u origin main
```

### 2. Repository Structure
```
retail-pricing-simulator/
├── .github/workflows/deploy.yml
├── backend/
│   ├── main.py
│   ├── pricing_model.py
│   ├── requirements.txt
│   └── ...
├── src/
│   ├── app/
│   ├── components/
│   └── ...
├── public/
├── README.md
├── LICENSE
└── package.json
```

### 3. Environment Setup

#### Frontend Environment Variables
Create `.env.local` in root:
```env
NEXT_PUBLIC_API_URL=https://your-backend-url.com
```

#### Backend Environment Variables
Create `.env` in backend folder:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/pricing_db
DEBUG=true
API_HOST=0.0.0.0
API_PORT=5000
```

### 4. Deployment Options

#### Option A: GitHub Pages (Frontend Only)
1. Push to main branch
2. GitHub Actions will automatically deploy to GitHub Pages
3. Backend needs separate deployment (Render, Heroku, etc.)

#### Option B: Full Stack Deployment
- **Frontend**: Vercel, Netlify, or GitHub Pages
- **Backend**: Render, Heroku, Railway, or AWS

### 5. Backend Deployment Services

#### Render (Recommended)
```bash
# Create render.yaml in backend folder
services:
  - type: web
    name: retail-pricing-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
```

#### Heroku
```bash
# Create Procfile in backend folder
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

### 6. GitHub Secrets
Add these secrets to your GitHub repository:
- `NEXT_PUBLIC_API_URL`: Your backend URL
- `DATABASE_URL`: PostgreSQL connection string
- `GITHUB_TOKEN`: Automatically provided

### 7. Database Setup (PostgreSQL)
```sql
CREATE DATABASE pricing_db;
CREATE USER pricing_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE pricing_db TO pricing_user;
```

### 8. Local Development
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/retail-pricing-simulator.git
cd retail-pricing-simulator

# Install dependencies
npm install
cd backend && pip install -r requirements.txt

# Start development servers
npm run dev  # Frontend
cd backend && python -m uvicorn main:app --reload  # Backend
```

### 9. Testing
```bash
# Run system tests
python test_system.py

# Test frontend
npm run build
npm run start

# Test backend
cd backend && python -m pytest
```

### 10. Monitoring
- **Frontend**: Vercel Analytics or Google Analytics
- **Backend**: Application monitoring with Sentry or similar
- **Database**: PostgreSQL monitoring

### 11. Custom Domain Setup
1. Add custom domain to your deployment service
2. Update CORS configuration in backend/main.py
3. Update NEXT_PUBLIC_API_URL in frontend

### 12. Security Checklist
- [ ] Environment variables properly configured
- [ ] CORS origins updated for production
- [ ] Database credentials secured
- [ ] API rate limiting implemented
- [ ] HTTPS enforced

### 13. Performance Optimization
- [ ] Enable gzip compression
- [ ] Implement caching
- [ ] Optimize images
- [ ] Database indexing
- [ ] CDN setup

### 14. Support & Maintenance
- Monitor GitHub Issues
- Regular dependency updates
- Performance monitoring
- Security patches

## 🎯 Quick Start Commands

```bash
# 1. Clone & Setup
git clone https://github.com/YOUR_USERNAME/retail-pricing-simulator.git
cd retail-pricing-simulator

# 2. Install Dependencies
npm install
cd backend && pip install -r requirements.txt

# 3. Start Development
npm run dev  # Frontend: http://localhost:8000
cd backend && python -m uvicorn main:app --reload  # Backend: http://localhost:5000

# 4. Test
python test_system.py
```

## 📞 Support
For issues or questions:
1. Check GitHub Issues
2. Review README.md
3. Check API documentation at /docs
4. Run system tests
