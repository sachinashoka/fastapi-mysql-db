"""
CRUD operations for database models.
"""
from sqlalchemy.orm import Session
from typing import List, Optional
import models
import schemas


# User CRUD operations
def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    """Create a new user in the database."""
    db_user = models.User(
        username=user.username,
        email=user.email,
        full_name=user.full_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int) -> Optional[models.User]:
    """Get a user by ID."""
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    """Get a user by username."""
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    """Get a user by email."""
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    """Get a list of users with pagination."""
    return db.query(models.User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate) -> Optional[models.User]:
    """Update a user's information."""
    db_user = get_user(db, user_id)
    if db_user is None:
        return None
    
    update_data = user_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> bool:
    """Delete a user from the database."""
    db_user = get_user(db, user_id)
    if db_user is None:
        return False
    
    db.delete(db_user)
    db.commit()
    return True


# Post CRUD operations
def create_post(db: Session, post: schemas.PostCreate) -> models.Post:
    """Create a new post in the database."""
    db_post = models.Post(
        title=post.title,
        content=post.content,
        author=post.author
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, post_id: int) -> Optional[models.Post]:
    """Get a post by ID."""
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100) -> List[models.Post]:
    """Get a list of posts with pagination."""
    return db.query(models.Post).offset(skip).limit(limit).all()


def get_posts_by_author(db: Session, author: str, skip: int = 0, limit: int = 100) -> List[models.Post]:
    """Get posts by a specific author."""
    return db.query(models.Post).filter(models.Post.author == author).offset(skip).limit(limit).all()


def update_post(db: Session, post_id: int, post_update: schemas.PostUpdate) -> Optional[models.Post]:
    """Update a post's information."""
    db_post = get_post(db, post_id)
    if db_post is None:
        return None
    
    update_data = post_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_post, field, value)
    
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int) -> bool:
    """Delete a post from the database."""
    db_post = get_post(db, post_id)
    if db_post is None:
        return False
    
    db.delete(db_post)
    db.commit()
    return True
