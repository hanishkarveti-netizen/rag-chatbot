import chromadb

from sentence_transformers import SentenceTransformer
from src.services.embeddings.embedding import model
from src.services.llm.llm import generate_answer


client = chromadb.PersistentClient(
    path="chromadb_data"
)

collection = client.get_collection(
    name="rag_collection"
)

def retrieve_chunks(query):

    print("\n")
    print("USER QUESTION")
    print(query)

    # Convert Question → Embedding
    query_embedding = model.encode(query)

    # Search ChromaDB
    results = collection.query(

        query_embeddings=[
            query_embedding.tolist()
        ],

        n_results=1
    )

    respones = generate_answer(query, results["documents"])
    print(respones)
    print("\n")
    print("SIMILAR CHUNKS")
    return results

    # for index, doc in enumerate(
    #     results["documents"][0]
    # ):

    #     print("\n")

    #     print(f"RESULT {index+1}")

    #     print(doc)

    # return results