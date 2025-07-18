from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    full_name: Mapped[str] = mapped_column(String(120), nullable=True)
    bio: Mapped[str] = mapped_column(String(200), nullable=True)
    profile_picture: Mapped[str] = mapped_column(String(255), nullable=True)
    website: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean(), default=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
            "bio": self.bio,
            "profile_picture": self.profile_picture,
            "website": self.website,
            "is_active": self.is_active,
            "is_verified": self.is_verified,
        }


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    image_url: Mapped[str] = mapped_column(String(255), nullable=False)
    caption: Mapped[str] = mapped_column(String(500), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "image_url": self.image_url,
            "caption": self.caption,
        }


class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(String(500), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "post_id": self.post_id,
            "user_id": self.user_id,
            "text": self.text,
        }


class Like(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "post_id": self.post_id,
            "user_id": self.user_id,
        }


class Follow(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    follower_id: Mapped[int] = mapped_column(nullable=False)
    followed_id: Mapped[int] = mapped_column(nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "follower_id": self.follower_id,
            "followed_id": self.followed_id,
        }
