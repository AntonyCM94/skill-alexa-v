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
def frase_random():
    prompt = "Dame una frase breve, motivadora y divertida en español, como si viniera de un amigo filósofo con sentido del humor."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        message=[
            {"role": "system", "content": "Eres un sabio que habla en español con tono cercano y humano."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=100
    )

    frase = response.choices[0].message.content
    return {"frase": frase}