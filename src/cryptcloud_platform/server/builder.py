from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from click import Group
from litestar.config.response_cache import ResponseCacheConfig, default_cache_key_builder
from litestar.plugins import CLIPluginProtocol, InitPluginProtocol
from litestar.security.jwt import Token
from litestar.stores.registry import StoreRegistry

if TYPE_CHECKING:
    from click import Group
    from litestar import Request
    from litestar.config.app import AppConfig
    
    
T = TypeVar("T")


class ApplicationConfigurator(InitPluginProtocol, CLIPluginProtocol):
    
    """
    Application Configurator
    Application configuration plugin
    """
    
    __slots__ = ("blank", "app_slug")
    
    app_slug: str
    
    def __init__(self) -> None:
        '''
        Initialize the application configurator
        
        ARGS:
            config: configure and start SAQ
        '''
        
    def on_cli_init(self, cli: Group) -> None:
        from ..cli.commands import user_management_app
        from ..config import get_settings
        
        settings = get_settings()
        
        self.app_slug = settings.app.APP_SLUG
        cli.add_command(user_management_app)