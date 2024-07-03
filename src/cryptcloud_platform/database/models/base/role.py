from __future__ import annotations

from typing import TYPE_CHECKING

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4
from ..user.user_role import UserRole


if TYPE_CHECKING:
    from .user import User
    from .team import Team
    

class Role:
    __tablename__ = "role"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(length=50), unique=True, nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(length=50), unique=True, nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(length=255), nullable=True)
    users: Mapped[list[User]] = relationship(
        back_populates="roles",
        secondary=lambda: UserRole.__table__,
        lazy="selectin",
    )
    
    
    