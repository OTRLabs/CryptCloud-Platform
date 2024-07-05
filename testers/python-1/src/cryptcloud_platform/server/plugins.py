from __future__ import annotations

from advanced_alchemy.exceptions.litestar import SQLAlchemyPlugin
from litestar.plugins.structlog import StructlogPlugin

from litestar_granian import GranianPlugin
from litestar_saq import SAQPlugin
from litestar_vite import VitePlugin

from ..config import app as config
from .builder import ApplicationConfigurator

structlog = StructlogPlugin(config=config.log)
vite = VitePlugin(config=config.vite)
saq = SAQPlugin(config=config.saq)
alchemy = SQLAlchemyPlugin(config=config.database)
granian = GranianPlugin()
app_config = ApplicationConfigurator()