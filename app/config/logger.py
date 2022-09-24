LOGGER_NAME: str = "merali"
LOG_FORMAT: str = "%(asctime)s\t%(levelname)s\t%(message)s"
LOG_LEVEL: str = "DEBUG"

# Logging config
version = 1
disable_existing_loggers = False

formatters = {
    "default": {
        "()": "uvicorn.logging.DefaultFormatter",
        "fmt": LOG_FORMAT,
        "datefmt": "%Y-%m-%d %H:%M:%S",
    },
}

handlers = {
    "default": {
        "formatter": "default",
        "class": "logging.StreamHandler",
        "stream": "ext://sys.stderr",
    },
}

loggers = {
    "": {"handlers": ["default"], "level": LOG_LEVEL, "propagate": False},
    "uvicorn": {"handlers": ["default"], "level": LOG_LEVEL, "propagate": False}
}
