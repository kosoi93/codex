"""Wrapper around an AI API such as OpenAI.

This class abstracts communication with the OpenAI API. It can be extended
for other providers by modifying :meth:`generate_response`.
"""

from __future__ import annotations

from typing import Optional

import openai


class AIClient:
    """Simple client for generating text using OpenAI's chat completions."""

    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo") -> None:
        openai.api_key = api_key
        self.model = model

    def generate_response(self, prompt: str) -> str:
        """Send the prompt to the AI service and return its response."""

        try:
            completion = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as exc:  # pragma: no cover - network errors
            # In production, proper logging should be done here.
            return f"Error contacting AI service: {exc}"

        choice: Optional[dict] = completion.choices[0] if completion.choices else None
        if not choice or "message" not in choice:
            return "No response from AI service"

        return choice["message"].get("content", "")
