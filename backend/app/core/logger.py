"""
Central logging configuration for ULTRA-Z.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

import colorlog

# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOG_DIRECTORY = PROJECT_ROOT / "storage" / "logs"
LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIRECTORY / "ultra_z.log"

# ---------------------------------------------------------------------
# Logger
# ---------------------------------------------------------------------

LOGGER_NAME = "ultra_z"

logger = logging.getLogger(LOGGER_NAME)

logger.setLevel(logging.INFO)

if not logger.handlers:

    # ---------------- Console ---------------- #

    console_handler = colorlog.StreamHandler()

    console_handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%H:%M:%S",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
        )
    )

    # ---------------- File ---------------- #

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
        )
    )

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

logger.propagate = False