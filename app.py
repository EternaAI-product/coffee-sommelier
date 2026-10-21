import os
from flask import Flask, render_template_string
from google import genai
from google.genai import types

app = Flask(__name__)

# Клиент с таймаутом, чтобы запрос не "висел"
client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=30000)
)

system_prompt = "Ты — профессиональный AI-ассистент Кофейный сомелье."

@app.route("/")
def home():
    try:
        # Используем актуальную стабильную модель
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents="Помоги выбрать кофе в зернах с ягодной кислинкой.",
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            )
        )
        answer = response.text
    except Exception as e:
        answer = f"Ошибка связи с API: {str(e)}"
    
    return render_template_string("<h1>AI-ассистент: Кофейный сомелье</h1><p>{{ answer }}</p>", answer=answer)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
