from fastapi import FastAPI, HTTPException
from typing import List
import json

app = FastAPI(
    title="AlphaPred API",
    description="Insights de arbitragem em mercados de previsão",
    version="1.0.0"
)from fastapi import FastAPI
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

@app.get("/signals", response_model=List[dict])
def get_signals():
    try:
        with open("data/signals.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Sinais não encontrados. O pipeline rodou?")