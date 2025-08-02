#!/usr/bin/env python3
"""
Simple test script for the FastAPI authentication system.
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_registration():
    """Test user registration."""
    print("🔐 Testing User Registration")
    print("-" * 40)
    
    # Test data
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/v1/auth/register", json=user_data)
        
        if response.status_code == 201:
            result = response.json()
            print("✅ Registration successful!")
            print(f"   User ID: {result['user_id']}")
            print(f"   Username: {result['username']}")
            print(f"   Email: {result['email']}")
            return True
        else:
            print(f"❌ Registration failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure it's running!")
        return False

def test_login():
    """Test user login."""
    print("\n🔑 Testing User Login")
    print("-" * 40)
    
    # Test data
    login_data = {
        "username": "testuser",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/v1/auth/login", json=login_data)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Login successful!")
            print(f"   Message: {result['message']}")
            print(f"   User ID: {result['user_id']}")
            return True
        else:
            print(f"❌ Login failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure it's running!")
        return False

def test_health_check():
    """Test server health."""
    print("\n🏥 Testing Server Health")
    print("-" * 40)
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Server is healthy!")
            print(f"   Status: {result['status']}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure it's running!")
        return False

if __name__ == "__main__":
    print("🚀 FastAPI Authentication Test")
    print("=" * 50)
    
    # Test server health first
    if not test_health_check():
        print("\n💡 Make sure your server is running:")
        print("   source .venv/bin/activate")
        print("   uvicorn app.main:app --reload")
        exit(1)
    
    # Test registration
    registration_success = test_registration()
    
    # Test login (only if registration was successful)
    if registration_success:
        test_login()
    
    print("\n🎉 Tests completed!")
    print("\n💡 Next steps:")
    print("   1. Visit http://localhost:8000/docs for API documentation")
    print("   2. Try the endpoints in the interactive docs")
    print("   3. Check the users.csv file to see stored user data")
