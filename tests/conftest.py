import os

# Must run BEFORE the app is imported: tests never call the real AI.
os.environ["MOCK_AI"] = "true"
os.environ["RATE_LIMIT_PER_MINUTE"] = "1000"
os.environ["DAILY_AI_CALL_LIMIT"] = "100000"

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)
