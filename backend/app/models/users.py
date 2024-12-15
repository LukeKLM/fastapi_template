from sqlalchemy import UUID
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from core.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(UUID, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(
        Text,
    )  # todo: possibly to change to varchar(1024) after implementation
    is_active = Column(Boolean, default=True)

