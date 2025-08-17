# Financial Advisory POC

A comprehensive proof of concept for a financial advisory application built with React and Node.js.

## Project Structure

```
financial-advisory-poc/
├── client/                 # React frontend
│   ├── public/
│   │   ├── index.html
│   │   └── manifest.json
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.js
│   │   │   ├── PortfolioAnalysis.js
│   │   │   ├── RiskAssessment.js
│   │   │   └── Navigation.js
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── utils/
│   │   │   └── calculations.js
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   └── package.json
├── server/                 # Node.js backend
│   ├── controllers/
│   │   ├── portfolioController.js
│   │   ├── riskController.js
│   │   └── userController.js
│   ├── models/
│   │   ├── Portfolio.js
│   │   ├── User.js
│   │   └── Investment.js
│   ├── routes/
│   │   ├── portfolio.js
│   │   ├── risk.js
│   │   └── users.js
│   ├── middleware/
│   │   └── auth.js
│   ├── config/
│   │   └── database.js
│   ├── server.js
│   └── package.json
├── shared/                 # Shared utilities
│   ├── constants.js
│   └── validators.js
└── README.md
```

## Features

### 1. Portfolio Management
- Real-time portfolio tracking
- Asset allocation visualization
- Performance analytics
- Rebalancing recommendations

### 2. Risk Assessment
- Risk tolerance questionnaire
- Volatility analysis
- Stress testing scenarios
- Risk-adjusted returns calculation

### 3. Financial Planning
- Goal-based planning
- Retirement projections
- Tax optimization strategies
- Cash flow analysis

### 4. Market Analysis
- Real-time market data integration
- Technical indicators
- Economic calendar
- Market sentiment analysis

## Technology Stack

### Frontend
- **React** - User interface framework
- **Chart.js** - Data visualization
- **Material-UI** - Component library
- **Axios** - HTTP client
- **Redux** - State management

### Backend
- **Node.js** - Runtime environment
- **Express.js** - Web framework
- **MongoDB** - Database
- **Mongoose** - ODM
- **JWT** - Authentication
- **Bcrypt** - Password hashing

### External APIs
- **Alpha Vantage** - Market data
- **Yahoo Finance** - Stock prices
- **Federal Reserve Economic Data (FRED)** - Economic indicators

## Installation

### Prerequisites
- Node.js (v14 or higher)
- MongoDB
- npm or yarn

### Setup

1. Clone the repository:
```bash
git clone https://github.com/HendrixLiangYH/test.git
cd test
```

2. Install server dependencies:
```bash
cd server
npm install
```

3. Install client dependencies:
```bash
cd ../client
npm install
```

4. Set up environment variables:
Create `.env` files in both server and client directories with required configurations.

5. Start the development servers:

Backend:
```bash
cd server
npm run dev
```

Frontend:
```bash
cd client
npm start
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout

### Portfolio
- `GET /api/portfolio` - Get user portfolio
- `POST /api/portfolio/add` - Add investment
- `PUT /api/portfolio/update/:id` - Update investment
- `DELETE /api/portfolio/remove/:id` - Remove investment

### Risk Assessment
- `POST /api/risk/assessment` - Submit risk questionnaire
- `GET /api/risk/profile/:userId` - Get risk profile
- `POST /api/risk/analysis` - Perform risk analysis

### Market Data
- `GET /api/market/quotes/:symbol` - Get stock quote
- `GET /api/market/historical/:symbol` - Get historical data
- `GET /api/market/indicators` - Get economic indicators

## Key Components

### Risk Assessment Algorithm
The risk assessment uses a multi-factor model considering:
- Time horizon
- Risk tolerance
- Investment experience
- Financial goals
- Market volatility preferences

### Portfolio Optimization
Implements Modern Portfolio Theory (MPT) for:
- Efficient frontier calculation
- Optimal asset allocation
- Risk-return optimization
- Correlation analysis

### Financial Calculations
- Compound Annual Growth Rate (CAGR)
- Sharpe Ratio
- Maximum Drawdown
- Value at Risk (VaR)
- Beta coefficient

## Development Guidelines

### Code Structure
- Follow ES6+ standards
- Use functional components with hooks
- Implement proper error handling
- Write unit tests for critical functions

### Security
- Input validation and sanitization
- JWT token authentication
- Rate limiting
- CORS configuration

### Performance
- Code splitting and lazy loading
- Memoization for expensive calculations
- Efficient database queries
- Caching strategies

## Testing

Run tests:
```bash
# Backend tests
cd server
npm test

# Frontend tests
cd client
npm test
```

## Deployment

### Production Build
```bash
# Build client
cd client
npm run build

# Prepare server
cd ../server
npm run build
```

### Environment Variables
Required environment variables:
- `MONGODB_URI`
- `JWT_SECRET`
- `ALPHA_VANTAGE_API_KEY`
- `NODE_ENV`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact [your-email@example.com]