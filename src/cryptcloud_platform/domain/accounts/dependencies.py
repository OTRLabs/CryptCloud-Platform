"""User Account Controllers."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sqlalchemy.orm import joinedload, load_only, selectinload


from ...database.models import Role, Team, TeamMember, UserRole
from app.db.models import User as UserModel
from app.domain.accounts.services import RoleService, UserRoleService, UserService
