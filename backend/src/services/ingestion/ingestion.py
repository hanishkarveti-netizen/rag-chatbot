from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

#loading pdf's are documents

def load_pdf(file_path):

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    return documents


def load_docx(file_path):

    loader = Docx2txtLoader(file_path)

    documents = loader.load()
    
    return documents

#Creating chunks
def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)
    
    # PRINT CHUNKS 
    for index, chunk in enumerate(chunks):

        print(f"CHUNK NUMBER : {index + 1}")

        print(chunk.page_content)
        print("/n")

    return chunks

