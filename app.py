import os
from flask import Flask, render_template_string
from google import genai

app = Flask(__name__)

# Клиент создается без лишних настроек, таймаут можно задать позже при необходимости
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

system_prompt = "Ты — профессиональный AI-ассистент Кофейный сомелье."

@app.route("/")
def home():
    try:
        # Используем новый метод interactions.create для актуальной модели
        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=f"{system_prompt}\n\nПомоги выбрать кофе в зернах с ягодной кислинкой."
        )
        answer = interaction.output_text
    except Exception as e:
        answer = f"Ошибка связи с API: {str(e)}"
    
    return render_template_string("<h1>AI-ассистент: Кофейный сомелье</h1><p>{{ answer }}</p>", answer=answer)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
