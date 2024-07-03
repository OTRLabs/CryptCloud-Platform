from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from litestar.config.response_cache import ResponseCacheConfig, default_cache_key_builder
from litestar.plugins import CLIPluginProtocol, InitPluginProtocol
from litestar.security.jwt import Token
from litestar.stores.registry import StoreRegistry

if TYPE_CHECKING:
    from click import Group
    from litestar import