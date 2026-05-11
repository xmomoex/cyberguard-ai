import re


def basic_url_analysis(url: str):
    score = 0
    reasons = []

    # 1. HTTPS
    if not url.startswith("https"):
        score += 20
        reasons.append("No usa HTTPS")

    # 2. IP en vez de dominio
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 40
        reasons.append("Usa IP en lugar de dominio")

    # 3. Palabras phishing
    phishing_words = [
        "login",
        "secure",
        "verify",
        "bank",
        "update",
        "account"
    ]

    for word in phishing_words:
        if word in url.lower():
            score += 10
            reasons.append(f"Contiene palabra sospechosa: {word}")

    # 4. URLs muy largas
    if len(url) > 75:
        score += 10
        reasons.append("URL demasiado larga")

    # Clasificación
    if score < 20:
        risk = "LOW"
    elif score < 50:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    return {
        "score": score,
        "risk": risk,
        "reasons": reasons
    }