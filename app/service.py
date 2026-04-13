from datetime import date
from app.models import HoroscopeRequest, HoroscopeResponse
from app.astro_engine import compute_signal, kerykeion_probe
from app.scoring import score_to_tone
from app.templates import build_sections


def normalize_period(req: HoroscopeRequest, mode: str) -> str:
    if req.date:
        return req.date
    today = date.today()
    if mode == "daily":
        return today.isoformat()
    if mode == "monthly":
        return today.strftime("%Y-%m")
    return today.strftime("%Y")


def generate(req: HoroscopeRequest, mode: str) -> HoroscopeResponse:
    period = normalize_period(req, mode)
    signal = compute_signal(req.sign, period, mode)
    tone = score_to_tone(signal["score"], req.language)
    sections = build_sections(req.sign, mode, signal["element"], signal["score"], req.language)
    return HoroscopeResponse(
        sign=req.sign,
        period=period,
        language=req.language,
        summary=tone["summary"],
        love=sections["love"],
        work=sections["work"],
        money=sections["money"],
        wellbeing=sections["wellbeing"],
        opportunities=tone["opportunities"],
        warnings=tone["warnings"],
        lucky_color=signal["lucky_color"],
        lucky_number=signal["lucky_number"],
        score=signal["score"],
    )


def diagnostics() -> dict:
    return {"kerykeion": kerykeion_probe()}
