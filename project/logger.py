"""Logging utilities for the Telegram bot project."""

from __future__ import annotations

import logging
from logging.config import dictConfig


_DEFAULT_LEVEL = logging.INFO


def setup_logging(level: int = _DEFAULT_LEVEL) -> None:
    """Configure basic logging for the application."""

    config = {
        "version": 1,
        "formatters": {
            "default": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": level,
            }
        },
        "root": {
            "handlers": ["console"],
            "level": level,
        },
    }
    dictConfig(config)


__all__ = ["setup_logging"]
