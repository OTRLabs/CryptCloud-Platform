import logging
from typing import cast

from advanced_alchemy.extensions.litestar import (
    AlembicAsyncConfig,
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    async_autocommit_before_send_handler,
)

from litestar.config.compression import CompressionConfig
from litestar.config.cors import CORSConfig
from litestar.config.csrf import CSRFConfig
from litestar.logging.config import LoggingConfig, StructLoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.plugins.structlog import StructlogConfig
from litestar_saq import CronJob, QueueConfig, SAQConfig
from litestar_vite import ViteConfig


from .base import get_settings

settings = get_settings()