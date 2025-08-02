from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from app.data.user_db_pandas import UserDb
import pandas as pd
import uuid

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Simple Pydantic models
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    user_id: str
    username: str
    email: str
    message: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate):
    """Register a new user - simple version."""
    df = UserDb.load_users()
    
    # Check if email already exists
    if not df.empty and user.email in df["email"].values:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Check if username already exists
    if not df.empty and user.username in df["username"].values:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    
    # Hash password and create new user
    hashed_password = pwd_context.hash(user.password)
    user_id = str(uuid.uuid4())
    
    new_user = {
        "user_id": user_id,
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
        "session_key": "",
        "last_login": "",
        "last_logout": ""
    }
    
    # Add new user to DataFrame
    df_row = pd.DataFrame([new_user])
    df_updated = pd.concat([df, df_row], ignore_index=True)
    UserDb.save_users(df_updated)
    
    return {
        "user_id": user_id,
        "username": user.username,
        "email": user.email,
        "message": "User registered successfully"
    }

@router.post("/login")
def login_user(user: UserLogin):
    """Login user - simple version."""
    df = UserDb.load_users()
    
    if df.empty:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No users found"
        )
    
    # Find user by username
    user_row = df[df["username"] == user.username]
    if user_row.empty:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    user_data = user_row.iloc[0].to_dict()
    
    # Verify password
    if not pwd_context.verify(user.password, user_data["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    return {
        "message": "Login successful",
        "user_id": user_data["user_id"],
        "username": user_data["username"]
    }
