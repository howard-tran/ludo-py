from datetime import datetime
from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    username = db.Column(String(500), nullable=False)
    password = db.Column(String(500), nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(
        DateTime, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )
    deleted_at = db.Column(DateTime, nullable=True)
