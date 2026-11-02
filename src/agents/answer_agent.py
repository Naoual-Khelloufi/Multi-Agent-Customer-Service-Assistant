from groq import Groq

from src.config import GROQ_API_KEY, LLM_MODEL_NAME


def answer_agent(state):

    question = state["question"]
    context = state.get("context", "")

    # Check if relevant context exists
    if not context.strip():
        return {
            "answer": "I could not find relevant information in the knowledge base.",
            "generation_status": "no_context"
        }

    # Check API key
    if not GROQ_API_KEY:
        return {
            "answer": "LLM generation is unavailable. Please configure your Groq API key.",
            "generation_status": "no_api_key"
        }

    try:
        client = Groq(api_key=GROQ_API_KEY)

        response = client.chat.completions.create(
            model=LLM_MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": """
You are a professional customer service assistant.

Answer the user's question using ONLY the information
provided in the context.

Instructions:
- Do not invent information.
- If the context does not contain the answer, say so clearly.
- Give clear, concise and practical answers.
- Use the same language as the user's question.
- Do not mention information that is not supported by the context.
"""
                },
                {
                    "role": "user",
                    "content": f"""
Context:
{context}

Question:
{question}

Answer:
"""
                }
            ],
            temperature=0.2,
            max_completion_tokens=500
        )

        answer = response.choices[0].message.content

        return {
            "answer": answer,
            "generation_status": "success"
        }

    except Exception as error:

        print(f"LLM API error: {error}")

        return {
            "answer": "I could not generate an answer at the moment. Please try again later.",
            "generation_status": "api_error"
        }