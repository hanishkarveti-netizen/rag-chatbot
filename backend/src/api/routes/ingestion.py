from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from src.services.ingestion.ingestion import split_document

router = APIRouter()

@router.get("/ingest")
def ingest_document(file: UploadFile = File(...), user_id: str = Form("anonymos")):
    response = split_document()
    return response