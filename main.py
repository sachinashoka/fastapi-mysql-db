"""
Main FastAPI application for MySQL database access.
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import routes
from database import engine, Base

# Load environment variables
load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title=os.getenv("APP_NAME", "FastAPI MySQL Application"),
    version=os.getenv("APP_VERSION", "1.0.0"),
    description="A FastAPI application for accessing MySQL database data",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routes.user_router)
app.include_router(routes.post_router)


@app.get("/", tags=["root"])
def read_root():
    """Root endpoint returning application information."""
    return {
        "message": "Welcome to FastAPI MySQL Application",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }


@app.get("/health", tags=["health"])
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    debug_mode = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=debug_mode
    )
