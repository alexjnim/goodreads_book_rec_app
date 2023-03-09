import os
import logging
import logging.config
from pathlib import Path

LOGGING_CONFIG_PATH = Path(__file__).resolve().parent / "logging.ini"

# configure logging with logging.ini
def get_logger():
    logging_config = os.environ.get("LOGGING_CONFIG", LOGGING_CONFIG_PATH)
    logging.config.fileConfig(logging_config, disable_existing_loggers=False)
    # ^ disable existing loggers = False as this might be loaded multiple times
    logger = logging.getLogger("main_logger")
    return logger
