import logging
import logging.config
import os
from pathlib import Path
from typing import Optional

import yaml

from boilerplate_module.config import (
    DEFAULT_LOG_FILE,
    DEFAULT_LOG_LEVEL,
    DEFAULT_OUTPUT_FOLDER,
    LOGGER_CONFIG_FILE,
)

CURRENT_DIR = Path(__file__).resolve().parent
REPO_ROOT = CURRENT_DIR.parent.parent

# e.g. /path/to/repo/logging.yml
LOGGER_CONFIG_FILE_PATH = REPO_ROOT / LOGGER_CONFIG_FILE


class ColorFormatter(logging.Formatter):
    # Define ANSI color codes as class-level constants
    COLORS = {
        logging.DEBUG: "\x1b[38;5;7m",  # Grey
        logging.INFO: "\x1b[38;5;46m",  # Green
        logging.WARNING: "\x1b[33;20m",  # Yellow
        logging.ERROR: "\x1b[31;20m",  # Red
        logging.CRITICAL: "\x1b[31;1m",  # Bold Red
    }
    RESET = "\x1b[0m"

    def __init__(self, fmt="%(message)s", datefmt="%Y-%m-%d %H:%M:%S"):
        super().__init__(fmt=fmt, datefmt=datefmt)
        self.default_fmt = fmt

    def format(self, record):
        # Set color based on the log level, defaulting to no color
        color = self.COLORS.get(record.levelno, "")
        log_fmt = f"{color}{self.default_fmt}{self.RESET}"

        # Temporarily set the formatter _style to the colorized version
        self._style._fmt = log_fmt
        return super().format(record)


def init_logger(loglevel: str = DEFAULT_LOG_LEVEL) -> None:
    """
    Initialize the logging configuration from a YAML file or default settings.

    It also changes the log level according to passed argument (e.g. from CLI),
    or environment variable if provided.
    Args:
        loglevel (str): Level of logging

    Returns:
        None
    """
    log_file_path = Path(DEFAULT_OUTPUT_FOLDER) / DEFAULT_LOG_FILE
    if not log_file_path.parent.exists():
        log_file_path.parent.mkdir(parents=True, exist_ok=True)

    if LOGGER_CONFIG_FILE_PATH.exists():
        with open(LOGGER_CONFIG_FILE_PATH, "rt", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig()

    set_level = logging.getLevelName(loglevel)
    logging.getLogger().setLevel(set_level)


def get_logger(loglevel: Optional[str] = None) -> logging.Logger:
    """
    Initialize the logger configuration and returns a logger instance.

    Args:
        loglevel (str): Level of logging

    Returns:
        logging.Logger: A configured logger instance.
    """
    # Set logging level with specified level from CLI or environment
    if loglevel is None:
        loglevel = os.environ.get("LOGGING_LEVEL")

    if loglevel is None:
        loglevel = DEFAULT_LOG_LEVEL

    init_logger(loglevel)
    logger = logging.getLogger(__name__)
    logger.info(f"Logger: {logger.name}.")
    return logger
