from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID  # noqa: TCH003

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy import UniqueConstraint


if TYPE_CHECKING:
    from ..base.user import User
    from ..user.user_role import UserRole
    from ..user.user_contact_info import UserContactInfo
    from ..base.organization import Organization
    from .organization_roles import OrganizationRole
    from ..organization.organization_team import OrganizationTeam
    
    
class OrganizationMember(UUIDAuditBase):
    __tablename__ = "organization_member"
    __table_args__ = (UniqueConstraint("organization_id", "user_id"),)
    organization_id: Mapped[UUID] = mapped_column(ForeignKey("organization.id", ondelete="cascade"), nullable=False)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id", ondelete="cascade"), nullable=False)
    role: Mapped[OrganizationRole] = mapped_column(
        String(length=50),
        default=OrganizationRole.MEMBER,
        nullable=False,
        index=True,
    )
    organization: Mapped["Organization"] = relationship(
        back_populates="members",
        foreign_keys="OrganizationMember.organization_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )
    user: Mapped["User"] = relationship(
        back_populates="organizations",
        foreign_keys="OrganizationMember.user_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )
    user_name: AssociationProxy[str] = association_proxy("user", "name")
    user_email: AssociationProxy[str] = association_proxy("user", "email")
    user_contact_info: Mapped[UserContactInfo] = relationship(
        back_populates="user",
        foreign_keys="OrganizationMember.user_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )
    user_roles: Mapped[UserRole] = relationship(
        back_populates="user",
        foreign_keys="OrganizationMember.user_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )
    user_teams: Mapped[OrganizationTeam] = relationship(
        back_populates="user",
        foreign_keys="OrganizationMember.user_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )

    def __repr__(self) -> str:
        return f"OrganizationMember(organization_id={self.organization_id}, user_id={self.user_id})"