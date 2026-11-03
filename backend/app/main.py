import os 
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv 

app = FastAPI(title=os.getenv("APP_NAME", "Hocnoto"))

@app.get("/api/health")
def health():
    return {"status": "ok"}