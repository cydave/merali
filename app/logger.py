import logging
import logging.config
from app.config import logger as logger_config

logging.config.dictConfig({k: getattr(logger_config, k) for k in dir(logger_config) if not k.startswith("_")})
logger = logging.getLogger("merali")
