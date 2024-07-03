from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from litestar import Litestar

def create_app() -> Litestar:
    '''create the asgi app'''
    
    from litestar import Litestar
    from litestar.di import Provide
    
    from .config import app as config
    
    from .config import constants
    from .config.base import get_settings
    
    from .domain.accounts import signals as accounts_signals
    from .domain.accounts.dependencies import provide_user
    from .domain.accounts.guards import auth
    
    #from .domain.teams import signals as teams_signals
    
    from .library.dependencies import create_collection_dependencies
    
    # from .server import openapi, plugins
    from .server import routers
    
    dependencies = {constants.USER_DEPENDENCY_KEY: Provide(provide_user)}
    dependencies.update(create_collection_dependencies())
    
    settings = get_settings()
    
    return Litestar(
        
        on_startup=[
            
        ],
        debug=settings.DEBUG,
        dependencies=dependencies,
        
        on_shutdown=[
            ## add function to kill k8s cluster
            ],
    )