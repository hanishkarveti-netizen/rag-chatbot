from fastapi import APIRouter, UploadFile, File
import shutil
import os

from src.services.ingestion.ingestion import (
    load_pdf,
    load_docx,
    split_documents
)

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"


    if file.filename.endswith(".pdf"):
        documents = load_pdf(file_path)

    elif file.filename.endswith(".docx"):
        documents = load_docx(file_path)

    else:
        return {
            "error": "Unsupported file type"
        }

    chunks = split_documents(documents)

    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "status": "Document chunked successfully"
    }
