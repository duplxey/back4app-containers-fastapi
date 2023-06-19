import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Back4app Containers rocks!"}


@app.get("/catfact")
def catfact():
    response = requests.get("https://catfact.ninja/fact")
    return {"fact": response.json()["fact"]}
