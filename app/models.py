from typing import Literal, Optional
from pydantic import BaseModel, Field

Sign = Literal[
    "aries","taurus","gemini","cancer","leo","virgo",
    "libra","scorpio","sagittarius","capricorn","aquarius","pisces"
]
Mode = Literal["daily", "monthly", "yearly"]
Language = Literal["ro", "en"]

class HoroscopeRequest(BaseModel):
    sign: Sign
    language: Language = "ro"
    date: Optional[str] = Field(default=None, description="YYYY-MM-DD for daily, YYYY-MM for monthly, YYYY for yearly")
    mode: Optional[Mode] = None

class HoroscopeResponse(BaseModel):
    sign: Sign
    period: str
    language: Language
    summary: str
    love: str
    work: str
    money: str
    wellbeing: str
    opportunities: str
    warnings: str
    lucky_color: str
    lucky_number: int
    score: int
