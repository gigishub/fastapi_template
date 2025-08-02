# FastAPI Authentication Template

A complete, production-ready FastAPI template with authentication, user management, and security best practices.

## 🚀 Features

- **User Authentication**: Register, login, logout with JWT tokens
- **Password Security**: Bcrypt password hashing
- **User Management**: User profiles and session management
- **Data Storage**: Pandas DataFrame with CSV persistence (easily upgradeable to databases)
- **API Documentation**: Automatic OpenAPI/Swagger documentation
- **CORS Support**: Cross-Origin Resource Sharing enabled
- **Environment Configuration**: Environment-based settings
- **Error Handling**: Proper HTTP status codes and error messages

## 📁 Project Structure

```
fast_api_template/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py        # Application settings
│   │   └── security.py      # Authentication utilities
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py       # API router
│   │       └── auth.py      # Authentication endpoints
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py          # Pydantic models
│   └── data/
│       ├── __init__.py
│       ├── user_db_pandas.py # User database operations
│       └── users.csv        # User data storage (auto-created)
├── tests/
│   └── __init__.py
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
├── test_auth.py            # Authentication test script
└── README.md               # This file
```

## 🛠️ Setup

### 1. Install Dependencies

```bash
# Create virtual environment (if not already created)
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

The `.env` file contains your application settings. Update the `SECRET_KEY` for production:

```env
SECRET_KEY="your-very-secure-secret-key-here"
```

### 3. Start the Server

```bash
uvicorn app.main:app --reload
```

Your API will be available at:
- **API**: http://localhost:8000
- **Documentation**: http://localhost:8000/docs
- **Alternative docs**: http://localhost:8000/redoc

## 🔐 API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Register a new user |
| POST | `/api/v1/auth/login` | Login user |
| POST | `/api/v1/auth/logout` | Logout user |
| GET | `/api/v1/auth/me` | Get current user info |

### General

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| GET | `/docs` | API documentation |

## 📝 Usage Examples

### Register a User

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

### Login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepassword123"
  }'
```

### Access Protected Endpoint

```bash
curl -X GET "http://localhost:8000/api/v1/auth/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 🧪 Testing

Run the included test script to verify everything works:

```bash
# Make sure your server is running first
uvicorn app.main:app --reload

# In another terminal, run the test
python test_auth.py
```

## 🔒 Security Features

- **Password Hashing**: Bcrypt with salt
- **JWT Tokens**: Secure token-based authentication
- **Token Expiration**: Configurable token lifetime
- **Input Validation**: Pydantic models validate all inputs
- **HTTPS Ready**: Easy to configure for production
- **CORS**: Configurable cross-origin support

## 🚀 Production Deployment

### Environment Variables

For production, set these environment variables:

```env
SECRET_KEY="your-super-secure-secret-key-minimum-32-characters"
DEBUG=false
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Database Migration

This template uses pandas/CSV for simplicity. For production, consider migrating to:

- **SQLite**: Simple file-based database
- **PostgreSQL**: Robust relational database
- **MySQL**: Popular relational database
- **MongoDB**: NoSQL document database

### Deployment Options

- **Docker**: Containerize the application
- **Heroku**: Easy cloud deployment
- **AWS**: EC2, Lambda, or ECS
- **DigitalOcean**: App Platform or Droplets
- **Vercel/Netlify**: Serverless deployment

## 📚 Next Steps

1. **Add More Endpoints**: Extend the API with your business logic
2. **Database Integration**: Replace pandas with a proper database
3. **Email Verification**: Add email confirmation for new users
4. **Password Reset**: Implement forgot password functionality
5. **Role-Based Access**: Add user roles and permissions
6. **Rate Limiting**: Implement API rate limiting
7. **Logging**: Add comprehensive logging
8. **Monitoring**: Set up health checks and monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter any issues:

1. Check the logs in your terminal
2. Verify all dependencies are installed
3. Ensure the server is running on the correct port
4. Check the `.env` file configuration

For more help, create an issue in the repository.
