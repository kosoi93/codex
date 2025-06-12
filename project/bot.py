"""Main bot entry point.

This module creates the Telegram bot instance, sets up all handlers and starts
polling. The bot token is intentionally stored here as per the repository
description. Replace ``YOUR_TOKEN`` with the actual bot token before running.
"""

from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Dict

import yaml
from aiogram import Bot, Dispatcher, Router

from .ai_client import AIClient
from .handlers import register_handlers
from .logger import setup_logging


# Insert your Telegram Bot API token here.
BOT_TOKEN = "YOUR_TOKEN"


def load_yaml(path: Path) -> Dict[str, str]:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


async def run() -> None:
    setup_logging()
    config = load_yaml(Path(__file__).with_name("config.yaml"))
    prompts = load_yaml(Path(__file__).with_name("prompts.yaml"))

    bot = Bot(BOT_TOKEN, parse_mode="HTML")
    router = Router()
    ai_client = AIClient(api_key="dummy")

    register_handlers(router, ai_client, prompts)

    dispatcher = Dispatcher()
    dispatcher.include_router(router)

    # Webhook support could be added here using `config`.
    await dispatcher.start_polling(bot)


def main() -> None:
    asyncio.run(run())

if __name__ == "__main__":
    main()
