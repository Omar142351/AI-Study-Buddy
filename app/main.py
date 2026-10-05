"""FastAPI app: validate -> check limits -> call AI service -> shape response.

Run it:   uvicorn app.main:app --reload
API docs: http://127.0.0.1:8000/docs
"""

import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException

from app import ai_service, config
from app.rate_limit import DailyBudget, RateLimiter
from app.schemas import StudyRequest, StudyResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-study-buddy")

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"

app = FastAPI(title="AI Study Buddy", version="1.0.0")

limiter = RateLimiter(config.RATE_LIMIT_PER_MINUTE, 60)
budget = DailyBudget(config.DAILY_AI_CALL_LIMIT)

# CORS is only needed if the frontend is hosted on a DIFFERENT origin than this API. (provided)
if config.ALLOWED_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.ALLOWED_ORIGINS,
        allow_methods=["GET", "POST"],
        allow_headers=["Content-Type"],
    )


# ---------------------------------------------------------------------------
# WEEK 1 - build the API
# ---------------------------------------------------------------------------

# TODO(W1-2): GET /health  ->  {"status": "ok", "ai_mode": config.ai_mode()}
#   Hint: @app.get("/health") above an async def.


# TODO(W1-3): POST /api/study
#   - takes a StudyRequest, returns a StudyResponse   (@app.post(..., response_model=StudyResponse))
#   - call:  result = await ai_service.study(payload)
#   - return StudyResponse(topic=payload.topic, mode=payload.mode, **result.model_dump())
#   Keep it thin: validate -> call service -> shape response.


# TODO(W1-4): make validation errors friendly.
#   Right now FastAPI answers bad input with 422 and a long list. We want:
#       status 400, body {"error": "topic: String should have at least 1 character"}
#   Hint: @app.exception_handler(RequestValidationError)
#         exc.errors()[0] has "loc" (where) and "msg" (what).
#         Remove the "Value error, " prefix from msg, then return JSONResponse({"error": ...}, status_code=400)


# ---------------------------------------------------------------------------
# WEEK 3 - make it safe
# ---------------------------------------------------------------------------

# TODO(W3-5): inside your /api/study function, BEFORE calling the AI:
#   ip = request.client.host if request.client else "unknown"      (add `request: Request` as a parameter)
#   wait = limiter.check(ip)
#   if wait: raise HTTPException(429, "Too many requests. Please slow down.", headers={"Retry-After": str(wait)})
#   if not budget.take(): raise HTTPException(429, "The daily study limit was reached. Try again tomorrow.")

# TODO(W3-6): map AI problems to safe messages (wrap your ai_service.study call):
#   except ai_service.AIUnavailable -> raise HTTPException(503, "The study buddy is not available right now.")
#   except ai_service.AIFailure     -> raise HTTPException(502, "The AI had a problem. Please try again.")
#   Never send exception details to the browser.

# TODO(W3-7): one error shape for everything.
#   Add @app.exception_handler(StarletteHTTPException) that returns
#   JSONResponse({"error": exc.detail}, status_code=exc.status_code, headers=exc.headers)


# ---------------------------------------------------------------------------
# The frontend (provided): FastAPI also serves your HTML/CSS/JS
# ---------------------------------------------------------------------------
@app.get("/", include_in_schema=False)
async def index():
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
