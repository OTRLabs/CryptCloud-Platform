from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.associationproxy import AssociationProxy


if TYPE_CHECKING:
    from ..base.user import User
    #from ..base.tag import Tag
    
    
    

class Organization(UUIDAuditBase):
    __tablename__ = "organization"
    __table_args__ = {"comment": "Organizations for application access"}
    
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String(length=500), nullable=True, default=None)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    members: Mapped[list[User]] = relationship(
        back_populates="organization",
        cascade="all, delete",
        passive_deletes=True,
        lazy="selectin",
    )
    '''tags: Mapped[list[Tag]] = relationship(
        secondary=lambda: organization_tag,
        back_populates="organizations",
        cascade="all, delete",
        passive_deletes=True,
    )'''

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    created_by: Mapped[User] = relationship(back_populates="organizations")
    created_by_name: AssociationProxy[str] = association_proxy("created_by", "name")
    created_by_email: AssociationProxy[str] = association_proxy("created_by", "email")
    __pii_columns__ = {"name"}
    
    def __repr__(self) -> str:
        return f"Organization(name={self.name})"
