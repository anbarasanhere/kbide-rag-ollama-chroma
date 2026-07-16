"""
Centralized logging configuration.
"""

import logging
import sys


class Logger:

    _logger = None

    @classmethod
    def get_logger(cls):

        if cls._logger is None:

            logger = logging.getLogger("KBIDE-AI")

            logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "[%(asctime)s] %(levelname)s - %(message)s",
                "%H:%M:%S"
            )

            console = logging.StreamHandler(sys.stdout)

            console.setFormatter(formatter)

            logger.addHandler(console)

            cls._logger = logger

        return cls._logger


logger = Logger.get_logger()
