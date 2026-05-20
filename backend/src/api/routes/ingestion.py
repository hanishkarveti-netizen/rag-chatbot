from fastapi import APIRouter, UploadFile, File
import shutil
import os

from src.services.ingestion.ingestion import (
    load_pdf,
    load_docx,
    split_documents,
    generate_embeddings,
    store_embeddings
)

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    # SAVE FILE
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # LOAD DOCUMENT
    if file.filename.endswith(".pdf"):

        documents = load_pdf(file_path)

    elif file.filename.endswith(".docx"):

        documents = load_docx(file_path)

    else:

        return {
            "error": "Unsupported file type"
        }

    # SPLIT DOCUMENT
    chunks = split_documents(documents)

    # CONVERT CHUNKS TO TEXT
    chunk_texts = []

    for chunk in chunks:

        chunk_texts.append(chunk.page_content)
    chunks = split_documents(documents)

    embeddings = generate_embeddings(chunks)
    vector_store = store_embeddings(chunks)
    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "chunks": chunk_texts
    }


# def print_split_document(split_documents , embedding_documents):
#     for index, chunk in enumerate(chunks):

#         print(f"CHUNK NUMBER : {index + 1}")

#         print(chunk.page_content)
#         print(embeddings)