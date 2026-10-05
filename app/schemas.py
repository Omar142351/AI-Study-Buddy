"""The API contract: what the browser may send and what it gets back.

WEEK 1 - you finish StudyRequest. StudyResult / StudyResponse are provided.
"""
from typing import Literal

from pydantic import BaseModel, Field, field_validator

Mode = Literal["explain", "example", "quiz", "summarize"]


class StudyRequest(BaseModel):
    mode: Mode

    # TODO(W1-1a): add the topic field
    #   topic: str, at least 1 and at most 200 characters
    # Hint: topic: str = Field(min_length=1, max_length=200)

    # TODO(W1-1b): add a validator that strips spaces from topic BEFORE the length rules run
    #   (so "   " counts as empty and is rejected).
    # Hint: @field_validator("topic", mode="before") + @classmethod
    #       return value.strip() if isinstance(value, str) else value


class StudyResult(BaseModel):
    """What the AI part produces. (provided)"""

    title: str
    answer: str
    key_points: list[str] = Field(default_factory=list, max_length=5)


class StudyResponse(StudyResult):
    """What the API returns: the AI result plus the request it belongs to. (provided)"""

    topic: str
    mode: Mode
