"""Application Modules"""
from __future__ import annotations

from typing import TYPE_CHECKING


## Import Controllers ##

from ..domain.web.controllers import WebController

if TYPE_CHECKING:
    from litestar.types import ControllerRouterHandler
    
route_handlers: list[ControllerRouterHandler] = [
    WebController,
    # Controllers
]