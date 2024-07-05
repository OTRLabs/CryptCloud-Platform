from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID  # noqa: TCH003

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
#from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy

if TYPE_CHECKING:
    from ..base.user import User
    
class UserContactInfo(UUIDAuditBase):
    __tablename__ = "user_contact_info"
    __table_args__ = {"comment": "User contact info"}
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user_account.id", ondelete="cascade"), nullable=False)
    user: Mapped[User] = relationship(back_populates="contact_info", innerjoin=True, uselist=False, lazy="joined")
    user_telegram: Mapped[str | None] = mapped_column(String(length=50), nullable=True, default=None)
    user_slack: Mapped[str | None] = mapped_column(String(length=50), nullable=True, default=None)
    user_discord: Mapped[str | None] = mapped_column(String(length=50), nullable=True, default=None)
    user_xmpp: Mapped[str | None] = mapped_column(String(length=50), nullable=True, default=None)    
    user_matrix: Mapped[str | None] = mapped_column(String(length=50), nullable=True, default=None)
    user_mastodon: Mapped[str | None] = mapped_column(String(length=50), nullable=True, default=None)
    user_twitter: Mapped[str | None] = mapped_column(String(length=50), nullable=True, default=None)
    
    def __repr__(self) -> str:
        return f"UserContactInfo(user_id={self.user_id}, user_telegram={self.user_telegram})"
    
    