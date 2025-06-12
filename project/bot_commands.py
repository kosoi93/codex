"""Utility functions and texts for common bot commands."""

from __future__ import annotations


HELP_TEXT = (
    "Available commands:\n"
    "/start - Welcome message\n"
    "/help - Show this help\n"
    "/about - Information about the bot"
)

ABOUT_TEXT = (
    "This is a simple Telegram bot that forwards your messages to an AI service "
    "and returns the generated response."
)

__all__ = ["HELP_TEXT", "ABOUT_TEXT"]
