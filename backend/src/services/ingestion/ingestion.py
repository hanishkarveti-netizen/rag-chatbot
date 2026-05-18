from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


def load_pdf(file_path):

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    return documents


def load_docx(file_path):

    loader = Docx2txtLoader(file_path)

    documents = loader.load()

    return documents


def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)
    
    # PRINT CHUNKS IN VS CODE TERMINAL
    for index, chunk in enumerate(chunks):

        print(f"CHUNK NUMBER : {index + 1}")

        print(chunk.page_content)

    return chunks
def generate_embeddings(chunks):
    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    embeddings = embedding_model.embed_documents(

        [chunk.page_content for chunk in chunks]

    )
    for index, vector in enumerate(embeddings):

        print(f"EMBEDDING {index+1}")

        print(vector[:10])
    return embeddings

# def print_split_document(split_documents , embedding_documents):
#     for index, chunk in enumerate(chunks):
#         for index, vector in enumerate(embeddings):
#             print(f"CHUNK NUMBER : {index + 1}")
#             print(chunk.page_content)
#             print(f"EMBEDDING {index+1}")
#             print(vector[:10])
