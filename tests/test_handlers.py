import types

import pytest

handlers = pytest.importorskip("project.handlers")
_format_prompt = handlers._format_prompt


@pytest.mark.parametrize(
    "text,prompts,expected",
    [
        ("hello", {"hello": "hi"}, "hi"),
        ("HELLO", {"hello": "hi"}, "hi"),
        ("unknown", {}, "unknown"),
    ],
)
def test_format_prompt(text, prompts, expected):
    assert _format_prompt(text, prompts) == expected
