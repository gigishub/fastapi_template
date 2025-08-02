# FastAPI Template - Simple Authentication

A clean, simple FastAPI template with basic authentication using pandas for data storage.

## 🚀 Quick Start

1. **Activate virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

2. **Start the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

3. **Test the system:**
   ```bash
   python test_simple_auth.py
   ```

## 📋 Features

- ✅ User registration with email validation
- ✅ Password hashing with bcrypt
- ✅ Simple login system
- ✅ Data storage using pandas/CSV
- ✅ API documentation at `/docs`
- ✅ Health check endpoint

## 🔗 API Endpoints

### Registration
```bash
POST /api/v1/auth/register
{
  "username": "your_username",
  "email": "your@email.com", 
  "password": "your_password"
}
```

### Login
```bash
POST /api/v1/auth/login
{
  "username": "your_username",
  "password": "your_password"
}
```

### Health Check
```bash
GET /health
```

## 📖 API Documentation

Visit `http://localhost:8000/docs` for interactive API documentation powered by Swagger UI.

## 🎯 Next Steps

You can easily extend this template by adding:
- JWT tokens for session management
- Password reset functionality
- User profile management
- Role-based access control
- Database integration (SQLite, PostgreSQL)
- Email verification
- Frontend integration
