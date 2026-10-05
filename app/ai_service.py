"""The only file that talks to the AI provider.
 
WEEK 3 - you write the real Gemini call in study(). Everything else is provided.
"""
 
import logging
 
from pydantic import ValidationError
 
from app import config
from app.prompts import SYSTEM, build_prompt
from app.schemas import StudyRequest, StudyResult
 
logger = logging.getLogger("ai-study-buddy")
 
 
class AIUnavailable(Exception):
    """The AI is not configured (no API key)."""
 
 
class AIFailure(Exception):
    """The AI was called but failed or returned something unusable."""
 
 
def mock_study(req: StudyRequest) -> StudyResult:
    """Fake answers so the app works with no key, no internet and no cost."""
    topic = getattr(req, "topic", "your topic")
    fake = {
        "explain": StudyResult(
            title=f"{topic} in simple words",
            answer=f"{topic} is easier than it sounds. (This is mock data.)\n\nCheck yourself: can you explain it to a friend?",
            key_points=["Start with the big idea", "Link it to something you know"],
        ),
        "example": StudyResult(
            title=f"Two ways to picture {topic}",
            answer="1. Like a team passing a ball.\n2. Like a recipe with steps. (mock data)",
            key_points=["Analogies make ideas stick"],
        ),
        "quiz": StudyResult(
            title=f"Quick quiz: {topic}",
            answer="Q1. What is the main idea?\nA) ...  B) ...  C) ...  D) ...\n\nAnswers: 1-B (mock data)",
            key_points=[],
        ),
        "summarize": StudyResult(
            title=f"{topic}: study notes",
            answer="Main idea: a one-sentence summary goes here. (mock data)",
            key_points=["Takeaway one", "Takeaway two", "Takeaway three"],
        ),
    }
    return fake[req.mode]
 
 
_client = None
 
 
def _get_client():
    """Create the Gemini client once, on first use."""
    global _client
    if _client is None:
        from google import genai
 
        _client = genai.Client(api_key=config.GEMINI_API_KEY)
    return _client
 
 
def _strip_fences(text: str) -> str:
    """Models sometimes wrap JSON in ```json fences even when told not to."""
    text = text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        text = text.removeprefix("json").strip()
    return text
 
 
async def study(req: StudyRequest) -> StudyResult:
    # Until you finish Week 3 this always returns fake data, so Weeks 1-2 work
    # with no API key and no cost.
    #
    # TODO(W3-2): replace the line below with the real logic:
    #   1. if config.MOCK_AI is true            -> return mock_study(req)
    #   2. if there is no config.GEMINI_API_KEY -> raise AIUnavailable("GEMINI_API_KEY is not set")
    #   3. otherwise call Gemini:
    #        from google.genai import types
    #        response = await _get_client().aio.models.generate_content(
    #            model=config.GEMINI_MODEL,
    #            contents=build_prompt(req),
    #            config=types.GenerateContentConfig(
    #                system_instruction=SYSTEM,
    #                response_mime_type="application/json",
    #                temperature=0.7,
    #            ),
    #        )
    #   4. turn response.text into a StudyResult:
    #        StudyResult.model_validate_json(_strip_fences(response.text or ""))
    #
    # TODO(W3-3): wrap step 3-4 in try/except
    #   except ValidationError -> log it, then raise AIFailure("unexpected format") from exc
    #   except Exception       -> logger.exception(...), then raise AIFailure(type(exc).__name__) from exc
    # Never put the user's text or the API key in a log message.
    return mock_study(req)