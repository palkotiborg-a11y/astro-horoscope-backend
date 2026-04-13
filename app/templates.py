def build_sections(sign: str, mode: str, element: str, score: int, language: str = "ro") -> dict:
    if language == "ro":
        return {
            "love": f"Pentru {sign}, zona relațională cere exprimare clară și reglaj emoțional; energia de tip {element} susține apropierea matură.",
            "work": f"În muncă, ritmul {mode} favorizează structurarea, selecția priorităților și execuția consecventă.",
            "money": f"Financiar, scorul actual {score}/100 indică prudență strategică și decizii mai bune când separi dorința de necesitate.",
            "wellbeing": "Ai rezultate mai bune dacă alternezi focusul intens cu pauze scurte și menții un program stabil de somn.",
        }
    return {
        "love": f"For {sign}, relationships benefit from clear expression and emotional regulation; {element} energy supports mature closeness.",
        "work": f"At work, the {mode} rhythm favors structure, priority selection, and consistent execution.",
        "money": f"Financially, the current score of {score}/100 suggests strategic caution and better decisions when you separate desire from necessity.",
        "wellbeing": "You do better when alternating intense focus with short breaks and maintaining stable sleep hygiene.",
    }
