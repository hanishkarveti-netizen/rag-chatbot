from sentence_transformers import SentenceTransformer

# Creating model
model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

# Creating embeddings

def generate_embeddings(chunks):
    chunk_texts = [
        chunk.page_content
        for chunk in chunks
    ]
    embeddings = model.encode(chunk_texts)

    print("Embeddings")
    # Printing embeddings
    for index, embedding in enumerate(embeddings):
        print(embedding)
        print("\n")
        
    return embeddings
