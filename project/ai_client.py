"""Wrapper around an AI API such as OpenAI."""

# TODO: Implement the client that communicates with the AI service.

class AIClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def generate_response(self, prompt: str) -> str:
        """Send the prompt to the AI service and return its response."""
        pass
