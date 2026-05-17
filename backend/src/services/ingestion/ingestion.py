from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings


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
    # for index, chunk in enumerate(chunks):

    #     print(f"CHUNK NUMBER : {index + 1}")

    #     print(chunk.page_content)

    return chunks
def embedding_documents(documents):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector = embeddings.embed_documents(documents)
    # print(vector)
    return vector

# def print_split_document(split_documents , embedding_documents):
#     for index, chunk in enumerate(chunks):

#         print(f"CHUNK NUMBER : {index + 1}")

#         print(chunk.page_content)
# print(vector)
