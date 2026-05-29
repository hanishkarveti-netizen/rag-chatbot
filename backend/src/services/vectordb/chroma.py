import chromadb

from chromadb.config import Settings


client = chromadb.PersistentClient(

    path="chromadb_data"
)


collection = client.get_or_create_collection(

    name="rag_collection"
)


def store_in_chromadb(chunks, embeddings):

    print("\n")

    print("=" * 60)
    print("STORING IN CHROMADB")
    print("=" * 60)

    for index, (chunk, embedding) in enumerate(

        zip(chunks, embeddings)
    ):

        collection.add(

            documents=[chunk.page_content],

            embeddings=[embedding.tolist()],

            ids=[f"id_{index}"]

        )

        print(f"STORED CHUNK : {index + 1}")

    print("\n")

    print("=" * 60)
    print("CHROMADB STORAGE COMPLETED")
    print("=" * 60)