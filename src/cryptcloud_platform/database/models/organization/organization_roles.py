from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID  # noqa: TCH003
from advanced_alchemy.mixins import UniqueMixin

# import slugify

from slugify import slugify

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship



if TYPE_CHECKING:
    from ..base.team import Team
    from ..user import User


class OrganizationRoles(UUIDAuditBase):
    """Organization Roles."""

    __tablename__ = "organization_roles"
    name: Mapped[str] = mapped_column(String(length=50), nullable=False, index=True)
    __table_args__ = (UniqueConstraint("name"),)

    def __repr__(self) -> str:
        return f"{self.name}"

    @property
    def slug(self) -> str:
        return slugify(self.name)

    @property
    def description(self) -> str:
        return self.name

    @property
    def users(self) -> AssociationProxy[list[User], User]:
        return association_proxy("organization", "users")

    @property
    def teams(self) -> AssociationProxy[list[Team], Team]:
        return association_proxy("organization", "teams")
    
    