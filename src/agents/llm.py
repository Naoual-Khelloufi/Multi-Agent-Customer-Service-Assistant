import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "openai/gpt-oss-20b"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto"
)


def generate_answer(prompt: str) -> str:
    messages = [
        {"role": "user", "content": prompt}
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    outputs = model.generate(
        inputs,
        max_new_tokens=400,
        do_sample=False
    )

    response = outputs[0][inputs.shape[-1]:]

    return tokenizer.decode(
        response,
        skip_special_tokens=True
    )