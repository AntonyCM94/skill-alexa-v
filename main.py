from fastapi import FastAPI
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "¡Hola desde tu skill Alexa con cerebro GPT!"}

@app.get("/frase")
def generar_frase():
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Dame una frase corta, sabia y divertida"}]
    )
    texto = respuesta.choices[0].message.content.strip()
    return {"frase": texto}
