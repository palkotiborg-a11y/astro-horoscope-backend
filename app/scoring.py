def score_to_tone(score: int, language: str = "ro") -> dict:
    if language == "ro":
        if score >= 85:
            return {
                "summary": "Perioadă foarte favorabilă pentru inițiativă, claritate și consolidare.",
                "opportunities": "Folosește impulsul pentru decizii importante și conversații-cheie.",
                "warnings": "Evită supraîncrederea și promisiunile prea largi.",
            }
        if score >= 75:
            return {
                "summary": "Perioadă bună, cu progres vizibil dacă rămâi disciplinat.",
                "opportunities": "Prioritizează sarcinile cu efect compus și finalizează ce ai început.",
                "warnings": "Nu risipi energia în detalii care nu schimbă rezultatul.",
            }
        return {
            "summary": "Perioadă mixtă, utilă pentru ajustări, nu pentru impulsivitate.",
            "opportunities": "Merg bine reviziile, reorganizarea și pașii mici, consistenți.",
            "warnings": "Ai grijă la reacții automate, grabă și concluzii fără verificare.",
        }
    else:
        if score >= 85:
            return {
                "summary": "A very favorable period for initiative, clarity, and consolidation.",
                "opportunities": "Use the momentum for important decisions and key conversations.",
                "warnings": "Avoid overconfidence and overly broad promises.",
            }
        if score >= 75:
            return {
                "summary": "A good period, with visible progress if you stay disciplined.",
                "opportunities": "Prioritize compounding tasks and finish what you started.",
                "warnings": "Do not waste energy on details that do not change the result.",
            }
        return {
            "summary": "A mixed period, better for adjustment than for impulsive moves.",
            "opportunities": "Reviews, reorganization, and small consistent steps work well.",
            "warnings": "Watch automatic reactions, haste, and unchecked conclusions.",
        }
