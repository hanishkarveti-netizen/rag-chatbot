from google import genai
# from src.services.retrieval.retrieval import retrieve_chunks


client = genai.Client(api_key="")

def generate_answer(

    question,

    retrieved_chunks

):
    context = retrieved_chunks

    prompt = f"""
You are a RAG assistant.

Use ONLY the provided context.

If the answer is not present in the context,
say:

'I could not find this information in the uploaded document.'

Context:

{context}
Question:

{question}
"""
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
    contents =  prompt
    )

    print(response.text)
