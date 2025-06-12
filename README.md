# Telegram AI Bot

This repository contains a minimal project structure for a Telegram bot that
uses an AI service (such as OpenAI) to respond to user messages.

## Project Layout

```
project/
├── bot.py            # Entry point that configures polling or webhook
├── handlers.py       # Handlers for button presses and routing
├── ai_client.py      # Wrapper over the AI API
├── logger.py         # Logging configuration
├── bot_commands.py   # Text for common commands
├── prompts.yaml      # Mapping from button labels to prompts
├── config.yaml       # Bot settings (token stored in bot.py)
└── requirements.txt  # Dependencies list
```

## Getting Started

1. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r project/requirements.txt
   ```
2. Set up your bot token inside `project/bot.py`.
3. Run the tests:
   ```bash
   pytest -q
   ```
4. Run the bot:
   ```bash
   python project/bot.py
   ```

## GitHub Tips

- Create issues to track features or bugs.
- Use Pull Requests for code review. Include clear descriptions and link to
  related issues.
- Configure branch protections if this is a collaborative project.

