from fastapi import APIRouter, UploadFile, File

import shutil
import os

from src.services.ingestion.ingestion import (
    load_pdf,
    load_docx,
    split_documents
)

from src.services.embeddings.embedding import (
    generate_embeddings
)

from src.services.vectordb.chroma import (
    store_in_chromadb
)

from src.services.retrieval.retrieval import retrieve_chunks


router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/ingest")
async def ingest_document(

    file: UploadFile = File(...)
):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    if file.filename.endswith(".pdf"):

        documents = load_pdf(file_path)

    elif file.filename.endswith(".docx"):

        documents = load_docx(file_path)

    else:

        return {
            "error": "Unsupported file type"
        }

    chunks = split_documents(documents)

    embeddings = generate_embeddings(chunks)

    store_in_chromadb(
        chunks,
        embeddings
    )

    return {

        "filename": file.filename,

        "total_chunks": len(chunks),

        "total_embeddings": len(embeddings),

        "status": "Stored in ChromaDB"
    }


@router.get("/query")
async def query_document(
    question: str
):
    results = retrieve_chunks(question)
    return {
        "question": question,
        "similar_chunks": results["documents"]
    }