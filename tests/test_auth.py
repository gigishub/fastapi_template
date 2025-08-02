"""
Test script to verify the FastAPI authentication system works correctly.
Run this after starting your server with: uvicorn app.main:app --reload
"""

import asyncio
import httpx

BASE_URL = "http://localhost:8000"

async def test_authentication():
    """Test the complete authentication flow."""
    
    async with httpx.AsyncClient() as client:
        print("🚀 Testing FastAPI Authentication System")
        print("=" * 50)
        
        # Test 1: Register a new user
        print("1. Testing user registration...")
        register_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
        }
        
        response = await client.post(f"{BASE_URL}/api/v1/auth/register", json=register_data)
        if response.status_code == 201:
            print("✅ User registration successful!")
            user_data = response.json()
            print(f"   User ID: {user_data['user_id']}")
            print(f"   Username: {user_data['username']}")
            print(f"   Email: {user_data['email']}")
        else:
            print(f"❌ Registration failed: {response.status_code} - {response.text}")
            return
        
        # Test 2: Login with the user
        print("\n2. Testing user login...")
        login_data = {
            "username": "testuser",
            "password": "testpassword123"
        }
        
        response = await client.post(f"{BASE_URL}/api/v1/auth/login", json=login_data)
        if response.status_code == 200:
            print("✅ User login successful!")
            token_data = response.json()
            access_token = token_data["access_token"]
            print(f"   Access token received (first 20 chars): {access_token[:20]}...")
        else:
            print(f"❌ Login failed: {response.status_code} - {response.text}")
            return
        
        # Test 3: Access protected route (get current user)
        print("\n3. Testing protected route...")
        headers = {"Authorization": f"Bearer {access_token}"}
        
        response = await client.get(f"{BASE_URL}/api/v1/auth/me", headers=headers)
        if response.status_code == 200:
            print("✅ Protected route access successful!")
            profile = response.json()
            print(f"   Username: {profile['username']}")
            print(f"   Email: {profile['email']}")
            print(f"   User ID: {profile['user_id']}")
        else:
            print(f"❌ Protected route failed: {response.status_code} - {response.text}")
        
        # Test 4: Logout
        print("\n4. Testing logout...")
        response = await client.post(f"{BASE_URL}/api/v1/auth/logout", headers=headers)
        if response.status_code == 200:
            print("✅ Logout successful!")
            print(f"   Message: {response.json()['message']}")
        else:
            print(f"❌ Logout failed: {response.status_code} - {response.text}")
        
        print("\n🎉 All tests completed!")

if __name__ == "__main__":
    print("Make sure your FastAPI server is running on http://localhost:8000")
    print("Run: uvicorn app.main:app --reload")
    print()
    
    try:
        asyncio.run(test_authentication())
    except httpx.ConnectError:
        print("❌ Could not connect to the server. Make sure it's running!")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
