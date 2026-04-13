from datetime import datetime
from typing import Any

try:
    from kerykeion import AstrologicalSubjectFactory
except Exception:
    AstrologicalSubjectFactory = None

SIGN_META = {
    "aries": {"element": "fire", "color": "red", "base": 76},
    "taurus": {"element": "earth", "color": "green", "base": 72},
    "gemini": {"element": "air", "color": "yellow", "base": 74},
    "cancer": {"element": "water", "color": "silver", "base": 71},
    "leo": {"element": "fire", "color": "gold", "base": 79},
    "virgo": {"element": "earth", "color": "olive", "base": 75},
    "libra": {"element": "air", "color": "pink", "base": 73},
    "scorpio": {"element": "water", "color": "burgundy", "base": 77},
    "sagittarius": {"element": "fire", "color": "purple", "base": 78},
    "capricorn": {"element": "earth", "color": "charcoal", "base": 80},
    "aquarius": {"element": "air", "color": "electric blue", "base": 74},
    "pisces": {"element": "water", "color": "sea green", "base": 70},
}


def kerykeion_probe() -> dict[str, Any]:
    if AstrologicalSubjectFactory is None:
        return {"enabled": False, "reason": "kerykeion import failed"}
    try:
        subject = AstrologicalSubjectFactory.from_birth_data(
            "Probe",
            1990, 1, 1, 12, 0,
            lng=23.6236, lat=46.7712, tz_str="Europe/Bucharest",
            online=False,
        )
        return {
            "enabled": True,
            "sun_sign": getattr(subject.sun, "sign", None),
            "moon_sign": getattr(subject.moon, "sign", None),
        }
    except Exception as e:
        return {"enabled": False, "reason": str(e)}


def period_seed(period: str) -> int:
    return sum(ord(c) for c in period) % 11


def compute_signal(sign: str, period: str, mode: str) -> dict:
    meta = SIGN_META[sign]
    seed = period_seed(period)
    mode_bonus = {"daily": 0, "monthly": 2, "yearly": 4}[mode]
    score = max(55, min(95, meta["base"] + seed - 5 + mode_bonus))
    return {
        "score": score,
        "element": meta["element"],
        "lucky_color": meta["color"],
        "lucky_number": (score % 9) + 1,
    }
