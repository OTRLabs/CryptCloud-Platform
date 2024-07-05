from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID  # noqa: TCH003
from advanced_alchemy.mixins import UniqueMixin

# import slugify

#from slugify import slugify

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship



from sqlalchemy import Column, String
from sqlalchemy.orm import relationship



class OrganizationRole(UUIDAuditBase):
    """Represents a role within an organization."""

    __tablename__ = "organization_roles"
    MEMBER = "MEMBER"
    ADMIN = "ADMIN"
    
    name = Column(String(50), unique=True, nullable=False, index=True)
    
    def __repr__(self) -> str:
        return f"{self.name}"
    
