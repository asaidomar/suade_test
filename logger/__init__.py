# -*- coding: utf-8; -*-
# alisaidomar <saidomarali@mail.com>

import os
import logging

from logging import config, getLogger
from logger import logger_config


try:
    config.dictConfig(logger_config.CONFIG)
except (ValueError, TypeError) as error:
    logging.exception(error)


def get_logger(name=None):
    log = getLogger(name=name)
    if os.environ.get("LOGLEVEL", None):
        log.setLevel(
            getattr(logging, os.environ.get("LOGLEVEL", "DEBUG"))
        )

    return log
