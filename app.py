import os
from flask import Flask, render_template_string
from google import genai

app = Flask(__name__)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

system_prompt = "Ты — профессиональный AI-ассистент Кофейный сомелье."

@app.route("/")
def home():
    try:
        # Используем самый базовый стабильный метод
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents="Помоги выбрать кофе в зернах с ягодной кислинкой."
        )
        answer = response.text
    except Exception as e:
        answer = f"Ошибка связи с API: {str(e)}"
    
    return render_template_string("<h1>AI-ассистент: Кофейный сомелье</h1><p>{{ answer }}</p>", answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
