"""Tiny in-memory limiters. Fine for one small server.

WEEK 3 - you implement RateLimiter.check(). DailyBudget is provided.
"""
import time
from collections import defaultdict, deque
from datetime import date


class RateLimiter:
    """Allow at most `max_calls` per `window_seconds` for each key (e.g. an IP address)."""

    def __init__(self, max_calls: int, window_seconds: int = 60):
        self.max_calls = max_calls
        self.window = window_seconds
        self._hits: dict[str, deque] = defaultdict(deque)

    def check(self, key: str, now: float | None = None) -> int:
        """Return 0 if allowed (and record the hit), else the number of seconds to wait."""
        # TODO(W3-4): implement this "sliding window"
        #   1. now = time.monotonic() if now is None
        #   2. hits = self._hits[key]
        #   3. remove timestamps older than the window from the LEFT of the deque (popleft)
        #   4. if len(hits) >= max_calls: return seconds until the oldest hit expires (at least 1)
        #   5. otherwise append(now) and return 0
        raise NotImplementedError("TODO(W3-4)")


class DailyBudget:
    """A global cap on AI calls per day, so a public site can never drain your quota."""

    def __init__(self, limit: int):
        self.limit = limit
        self._day = date.today()
        self._used = 0

    def take(self) -> bool:
        today = date.today()
        if today != self._day:
            self._day, self._used = today, 0
        if self._used >= self.limit:
            return False
        self._used += 1
        return True
