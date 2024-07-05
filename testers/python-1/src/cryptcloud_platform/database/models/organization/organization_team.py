from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID  # noqa: TCH003

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .organization_roles import OrganizationRole

if TYPE_CHECKING:
    from ..base.team import Team
    from ..base.organization import Organization
    #from ..user import User


class OrganizationTeam(UUIDAuditBase):
    __tablename__ = "organization_team"
    __table_args__ = (UniqueConstraint("organization_id", "team_id"),)
    organization_id: Mapped[UUID] = mapped_column(ForeignKey("organization.id", ondelete="cascade"), nullable=False)
    team_id: Mapped[UUID] = mapped_column(ForeignKey("team.id", ondelete="cascade"), nullable=False)
    role: Mapped[OrganizationRole] = mapped_column(
        String(length=50),
        default=OrganizationRole.MEMBER,
        nullable=False,
        index=True,
    )
    organization: Mapped["Organization"] = relationship(
        back_populates="teams",
        foreign_keys="OrganizationTeam.organization_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )
    team: Mapped[Team] = relationship(
        back_populates="organizations",
        foreign_keys="OrganizationTeam.team_id",
        innerjoin=True,
        uselist=False,
        lazy="joined",
    )
    name: AssociationProxy[str] = association_proxy("team", "name")
    slug: AssociationProxy[str] = association_proxy("team", "slug")

    def __repr__(self) -> str:
        return f"OrganizationTeam(organization_id={self.organization_id}, team_id={self.team_id})"
    
    def __str__(self) -> str:
        return f"OrganizationTeam(organization_id={self.organization_id}, team_id={self.team_id})"
    
    
    