"""Logger"""

import logging.config

import yaml

from src.core.colored_formatter import replace_formatter
from src.core.config import log_filename

with open(log_filename, 'r') as file:
    logger_config = yaml.safe_load(file)
    logging.config.dictConfig(logger_config)

logger = logging.getLogger()

# Replace root_formatter with colored_formatter
replace_formatter(logger)
