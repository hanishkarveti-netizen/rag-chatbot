# src/main.py

from fastapi import FastAPI
from src.api.routes.ingestion import router as ingestion_router
import uvicorn
app = FastAPI()

app.include_router(ingestion_router)
if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)