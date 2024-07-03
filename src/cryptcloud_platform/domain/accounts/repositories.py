from __future__ import annotations

from advanced_alchemy.repository import SQLAlchemyAsyncRepository, SQLAlchemyAsyncSlugRepository

from ...database.models.base.role import Role
from ...database.models.base.user import User
from ...database.models.user.user_role import UserRole


class UserRepository(SQLAlchemyAsyncRepository[User]):
    """User SQLAlchemy Repository."""

    model_type = User


class RoleRepository(SQLAlchemyAsyncSlugRepository[Role]):
    """User SQLAlchemy Repository."""

    model_type = Role


class UserRoleRepository(SQLAlchemyAsyncRepository[UserRole]):
    """User Role SQLAlchemy Repository."""

    model_type = UserRole