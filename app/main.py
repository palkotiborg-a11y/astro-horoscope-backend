from fastapi import FastAPI
from app.models import HoroscopeRequest
from app.service import generate, diagnostics
from fastmcp import FastMCP

app = FastAPI(title="Astro Horoscope Backend", version="0.1.0")
mcp = FastMCP("AstroHoroscopeMCP")

@app.get("/health")
def health():
    return {"status": "ok", **diagnostics()}

@app.post("/api/horoscope/daily")
def daily(req: HoroscopeRequest):
    return generate(req, "daily")

@app.post("/api/horoscope/monthly")
def monthly(req: HoroscopeRequest):
    return generate(req, "monthly")

@app.post("/api/horoscope/yearly")
def yearly(req: HoroscopeRequest):
    return generate(req, "yearly")

@mcp.tool
def get_horoscope(sign: str, mode: str = "daily", date: str | None = None, language: str = "ro"):
    req = HoroscopeRequest(sign=sign, date=date, language=language)
    return generate(req, mode).model_dump()

app.mount("/mcp", mcp.http_app())
