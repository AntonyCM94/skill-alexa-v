from fastapi import FastAPI
import openai
import os

open.api_key = os.getenv("OPEN_API_KEY")

app = FastAPI()

@app.get("/frase")
def generar_fase():
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": "Dame una frase original, filosofica y con humor"
        }]
    )
    texto = respuesta.choices[0].message.content.strip()
    return {"frase": texto}