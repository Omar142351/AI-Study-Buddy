"""Run with:  pytest -q

WEEK 1: make test_health pass.  WEEK 4: write the three tests marked TODO(W4-1).
"""
import pytest


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


# TODO(W4-1a): happy path
#   POST /api/study with {"topic": "Photosynthesis", "mode": "quiz"}
#   assert status 200, and that the body has a "title", an "answer" and a "key_points" list.


# TODO(W4-1b): error path
#   POST /api/study with {"topic": "   ", "mode": "explain"}
#   assert status 400 and that the "error" message mentions "topic".


# TODO(W4-1c): parametrized bad input
#   Use @pytest.mark.parametrize with at least 4 bad payloads
#   (empty topic, unknown mode, topic of 201 chars, missing topic)
#   and assert each one returns 400 with a string "error".
