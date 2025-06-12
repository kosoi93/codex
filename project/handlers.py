"""Message and command handlers for the Telegram bot.

The functions defined here are responsible for reacting to Telegram updates.
They are registered in :mod:`bot` and make use of :class:`AIClient` to
generate replies.
"""

from __future__ import annotations

from typing import Any, Dict

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from .ai_client import AIClient
from .bot_commands import HELP_TEXT, ABOUT_TEXT


async def handle_start(message: Message) -> None:
    """Send a welcome message with instructions."""

    await message.answer(
        "Hello! Send me a message and I'll ask the AI to respond."
    )


def _format_prompt(text: str, prompts: Dict[str, str]) -> str:
    return prompts.get(text.lower(), text)


def register_handlers(router: Router, ai_client: AIClient, prompts: Dict[str, str]) -> None:
    """Register bot commands and message handlers."""

    @router.message(CommandStart())
    async def start(message: Message) -> None:
        await handle_start(message)

    @router.message(Command("help"))
    async def help_cmd(message: Message) -> None:
        await message.answer(HELP_TEXT)

    @router.message(Command("about"))
    async def about_cmd(message: Message) -> None:
        await message.answer(ABOUT_TEXT)

    @router.message(F.text)
    async def echo(message: Message) -> None:
        prompt = _format_prompt(message.text, prompts)
        response = ai_client.generate_response(prompt)
        await message.answer(response)
