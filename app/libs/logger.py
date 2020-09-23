from os import getenv

import logging
# <~> Logging <~>
logging.basicConfig(filename="log_history.log",
                    level=logging.INFO)
# - Create handler for new log format
HANDLER = logging.StreamHandler()
HANDLER.setFormatter(
    fmt=logging.Formatter("%(asctime)s [%(levelname)-0s] %(name)s - %(message)s")
)
HANDLER.setLevel(level=getattr(logging, getenv("LOG_LEVEL", "INFO").upper()))

# - Updated root logger settings
logging.getLogger().handlers = []
logging.getLogger().addHandler(hdlr=HANDLER)

BASE_LOGGER = logging.getLogger("route")
BASE_LOGGER.setLevel(level=HANDLER.level)
