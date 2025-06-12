from __future__ import annotations

import pytest

ai_client = pytest.importorskip("project.ai_client")


class DummyCompletion:
    def __init__(self, content: str):
        self.choices = [{"message": {"content": content}}]


def fake_create(*args, **kwargs):
    return DummyCompletion("result")


@pytest.fixture
def patch_openai(monkeypatch):
    monkeypatch.setattr(ai_client.openai.ChatCompletion, "create", fake_create)


def test_generate_response(patch_openai):
    client = ai_client.AIClient(api_key="x")
    resp = client.generate_response("prompt")
    assert resp == "result"
