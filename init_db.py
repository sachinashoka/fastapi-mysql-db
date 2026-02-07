"""
Sample data initialization script for FastAPI MySQL application.
This script demonstrates how to create sample users and posts.
"""
import sys
from database import SessionLocal, engine, Base
from models import User, Post
from datetime import datetime

def init_sample_data():
    """Initialize the database with sample data."""
    
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    
    # Create a database session
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing_users = db.query(User).count()
        if existing_users > 0:
            print("Database already contains data. Skipping initialization.")
            return
        
        # Create sample users
        users = [
            User(
                username="johndoe",
                email="john@example.com",
                full_name="John Doe"
            ),
            User(
                username="janedoe",
                email="jane@example.com",
                full_name="Jane Doe"
            ),
            User(
                username="bobsmith",
                email="bob@example.com",
                full_name="Bob Smith"
            ),
        ]
        
        db.add_all(users)
        db.commit()
        print(f"Created {len(users)} sample users.")
        
        # Create sample posts
        posts = [
            Post(
                title="Getting Started with FastAPI",
                content="FastAPI is a modern, fast web framework for building APIs with Python 3.6+",
                author="johndoe"
            ),
            Post(
                title="MySQL Database Integration",
                content="Learn how to integrate MySQL with your FastAPI application using SQLAlchemy ORM",
                author="johndoe"
            ),
            Post(
                title="RESTful API Best Practices",
                content="Follow these best practices when designing RESTful APIs for your applications",
                author="janedoe"
            ),
            Post(
                title="Python Type Hints and Pydantic",
                content="Pydantic uses Python type hints for data validation and settings management",
                author="janedoe"
            ),
            Post(
                title="Asynchronous Programming in Python",
                content="Understanding async/await and how to use it effectively in your applications",
                author="bobsmith"
            ),
        ]
        
        db.add_all(posts)
        db.commit()
        print(f"Created {len(posts)} sample posts.")
        
        print("\nSample data initialization completed successfully!")
        print(f"Total users: {db.query(User).count()}")
        print(f"Total posts: {db.query(Post).count()}")
        
    except Exception as e:
        print(f"Error initializing sample data: {e}")
        db.rollback()
        sys.exit(1)
    finally:
        db.close()


if __name__ == "__main__":
    print("Initializing database with sample data...")
    init_sample_data()
