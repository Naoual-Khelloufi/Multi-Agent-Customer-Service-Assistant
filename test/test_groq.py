from groq import Groq
from src.config import GROQ_API_KEY, LLM_MODEL_NAME


client = Groq(api_key=GROQ_API_KEY)

response = client.chat.completions.create(
    model=LLM_MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": "Explain in two sentences how to handle an angry customer."
        }
    ],
    temperature=0.3,
    max_completion_tokens=150
)

print("\nLLM Response:")
print(response.choices[0].message.content)