# Astro Horoscope Backend

Self-hosted horoscope backend for Perplexity / Comet usage.

## Stack
- Python 3.11+
- FastAPI REST API
- FastMCP HTTP wrapper
- Kerykeion astrology engine
- Render deployment

## Goals
- Daily, monthly, yearly horoscope generation
- Romanian and English output
- Deterministic local logic
- MCP-compatible remote endpoint

## Quick start
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

## Local test
```bash
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/api/horoscope/daily -H "Content-Type: application/json" -d "{\"sign\":\"leo\",\"language\":\"ro\"}"
```

## Render deploy
1. Push this repo to GitHub.
2. In Render, create a new Blueprint or Web Service from the repo.
3. Render reads `render.yaml` from the repo root.
4. After deploy, your public URL will be like `https://your-service.onrender.com`.
5. MCP endpoint target in Perplexity should be `https://your-service.onrender.com/mcp`.

## Perplexity connector
- Settings
- Connectors
- Add custom remote connector
- URL: `https://your-service.onrender.com/mcp`
- Auth: None initially
- Transport: Streamable HTTP if offered

## Notes
The current logic is production-shaped but still heuristic. Replace `scoring.py` rules with richer transit weighting as you mature the engine.
