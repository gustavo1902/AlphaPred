from fastapi import FastAPI
from scripts.run_pipeline import run

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/signals")
def signals():
    return run()