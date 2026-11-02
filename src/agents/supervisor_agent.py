
def supervisor_agent(state):
    question = state.get("question", "")

    # Check whether the user submitted a valid question
    if not question.strip():
        return {
            "next_step": "end",
            "supervisor_message": "No question provided."
        }

    # Route valid questions to the retrieval agent
    return {
        "next_step": "retrieve",
        "supervisor_message": "Question accepted. Starting document retrieval."
    }
