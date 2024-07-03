from __future__ import annotations

from datetime import datetime  # noqa: TCH003
from uuid import UUID  # noqa: TCH003
import msgspec
from typing import Optional

from ...database.models.team.team_roles import TeamRoles
from ...library.schema import CamelizedBaseStruct

__all__ = (
    "AccountLogin",
    "AccountRegister",
    "UserRoleAdd",
    "UserRoleRevoke",
    "UserCreate",
    "User",
    "UserRole",
    "UserTeam",
    "UserUpdate",
    #"UserContactInfo",
)

class UserTeam(CamelizedBaseStruct):
    '''Holds team details for a user
    
    this is nested in the User model for "team"
    '''
    team_id: UUID
    team_name: str
    is_owner: bool
    role: TeamRoles = TeamRoles.MEMBER
    
class UserRole(CamelizedBaseStruct):
    """Holds role details for a user.

    This is nested in the User Model for 'roles'
    """

    role_id: UUID
    role_slug: str
    role_name: str
    assigned_at: datetime



class User(CamelizedBaseStruct):
    """User properties to use for a response."""

    id: UUID
    email: str
    name: str | None = None
    is_superuser: bool = False
    is_active: bool = False
    is_verified: bool = False
    teams: list[UserTeam] = []
    roles: list[UserRole] = []


class UserCreate(CamelizedBaseStruct):
    email: str
    password: str
    name: str | None = None
    is_superuser: bool = False
    is_active: bool = True
    is_verified: bool = False


class UserUpdate(CamelizedBaseStruct, omit_defaults=True):
    """User properties to use for a response."""

    email: Optional[str] = msgspec.UNSET
    password: Optional[str] = msgspec.UNSET
    name: Optional[str] = msgspec.UNSET
    is_superuser: Optional[bool] = msgspec.UNSET
    is_active: Optional[bool] = msgspec.UNSET
    is_verified: Optional[bool] = msgspec.UNSET

class AccountLogin(CamelizedBaseStruct):
    username: str
    password: str


class AccountRegister(CamelizedBaseStruct):
    email: str
    password: str
    name: str | None = None


class UserRoleAdd(CamelizedBaseStruct):
    """User role add ."""

    user_name: str


class UserRoleRevoke(CamelizedBaseStruct):
    """User role revoke ."""

    user_name: str