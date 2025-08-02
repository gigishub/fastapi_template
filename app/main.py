from fastapi import FastAPI
from app.api.v1.auth import router as auth_router

app = FastAPI(
    title="FastAPI Template",
    description="A simple FastAPI template with authentication",
    version="1.0.0"
)

# Include auth router
app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Template"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
