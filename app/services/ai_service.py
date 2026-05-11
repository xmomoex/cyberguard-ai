from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_ai_explanation(url: str, analysis: dict):

    prompt = f"""
Eres un experto en ciberseguridad y phishing.

Analiza esta URL:

URL: {url}

Resultado técnico:
- Riesgo: {analysis['risk']}
- Score: {analysis['score']}
- Razones: {analysis['reasons']}

Explica:
1. Por qué puede ser peligrosa
2. Qué riesgos tiene
3. Qué ocurriría si el usuario entra
4. Recomendación clara
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un experto en ciberseguridad."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generando respuesta IA: {str(e)}"