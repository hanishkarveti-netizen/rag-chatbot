import chromadb

from sentence_transformers import SentenceTransformer


client = chromadb.PersistentClient(
    path="chromadb_data"
)

collection = client.get_collection(
    name="rag_collection"
)

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def retrieve_chunks(query):

    print("\n")
    print("=" * 60)
    print("USER QUESTION")
    print("=" * 60)
    print(query)

    # Convert Question → Embedding
    query_embedding = model.encode(query)

    # Search ChromaDB
    results = collection.query(

        query_embeddings=[
            query_embedding.tolist()
        ],

        n_results=3
    )

    print("\n")
    print("=" * 60)
    print("SIMILAR CHUNKS")
    print("=" * 60)

    for index, doc in enumerate(
        results["documents"][0]
    ):

        print("\n")

        print(f"RESULT {index+1}")

        print(doc)

    return results