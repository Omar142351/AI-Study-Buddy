"""All settings live here. Values come from environment variables (.env locally)."""
import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")

# MOCK_AI=true -> never call Gemini, return built-in fake answers (free, offline).
MOCK_AI = os.getenv("MOCK_AI", "false").lower() == "true"

# Comma-separated list of browser origins allowed to call the API from another site.
# Empty (default) = same-origin only, which is what we want when FastAPI serves the UI.
ALLOWED_ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "").split(",") if o.strip()]

# Protect your key on a public website.
RATE_LIMIT_PER_MINUTE = int(os.getenv("RATE_LIMIT_PER_MINUTE", "8"))
DAILY_AI_CALL_LIMIT = int(os.getenv("DAILY_AI_CALL_LIMIT", "200"))


def ai_mode() -> str:
    """Which AI backend is active right now: 'mock', 'gemini' or 'unconfigured'."""
    if MOCK_AI:
        return "mock"
    return "gemini" if GEMINI_API_KEY else "unconfigured"
