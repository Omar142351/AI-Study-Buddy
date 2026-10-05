# AI Study Buddy

An AI web app that explains any topic in simple words, gives you examples, quizzes you, and writes study notes.

**Live app:** _TODO(W4-2): paste your Render URL here_

```
Browser (HTML/CSS/JS)  ->  FastAPI (validate, limit)  ->  Gemini  ->  JSON  ->  Browser
```

The Gemini key lives only on the server. It is never in the browser code and never in Git.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate            # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
cp .env.example .env                 # Windows: copy .env.example .env
```

`.env` starts with `MOCK_AI=true`, so everything works with **no API key**. You switch to the real AI in Week 3.

## Run

```bash
uvicorn app.main:app --reload
```

- App: http://127.0.0.1:8000
- Interactive API docs: http://127.0.0.1:8000/docs

## Test

```bash
pytest -q
```

## Your tasks

Find every task by searching the project for `TODO(` (VS Code: Cmd/Ctrl+Shift+F).

| Week | Goal | TODOs | Done when |
|------|------|-------|-----------|
| 1 | API works | W1-1 to W1-4 | `/health` and `/docs` work, `pytest` shows `test_health` passing |
| 2 | UI works | W2-1 to W2-6 | The page shows fake study results, with loading + error states |
| 3 | Real AI, safely | W3-1 to W3-7 | Real Gemini answers; rate limit works; no secret in the browser |
| 4 | Ship it | W4-1, W4-2 | Tests pass, code on GitHub, app live on Render |

Full instructions: the `guide/` folder your instructor gave you.

## Definition of done

- [ ] 4 modes work: explain, example, quiz, summarize
- [ ] Bad input gets a friendly 400 message
- [ ] The UI shows loading, success and error states
- [ ] The API key is never sent to the browser and never committed
- [ ] At least one happy-path and one error-path test pass
- [ ] The app is live and the URL is in this README

## Project map

```
app/main.py         routes + error handling        (Week 1, 3)
app/schemas.py      the request/response contract  (Week 1)
app/ai_service.py   the only file that calls Gemini (Week 3)
app/prompts.py      the prompts                    (Week 3)
app/rate_limit.py   abuse protection               (Week 3)
app/config.py       settings from environment
static/             index.html, app.js, style.css  (Week 2)
tests/              pytest tests                   (Week 1, 4)
render.yaml         deploy settings for Render
```
