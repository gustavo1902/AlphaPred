from fastapi import FastAPI
from scripts.run_pipeline import run
import json

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/signals")
def signals():
    with open("data/signals.json") as f:
        return json.load(f)