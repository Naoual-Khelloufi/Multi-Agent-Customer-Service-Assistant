
def validation_agent(state):
    answer = state.get("answer", "")
    context = state.get("context", "")
    sources = state.get("sources", [])
    generation_status = state.get("generation_status", "")

    # Check whether an answer was generated
    if not answer.strip():
        return {
            "validation_status": "failed",
            "validation_message": "No answer was generated."
        }

    # Check whether relevant context was retrieved
    if not context.strip() or not sources:
        return {
            "validation_status": "failed",
            "validation_message": "No supporting information was retrieved."
        }

    # Check whether generation was successful
    if generation_status != "success":
        return {
            "validation_status": "failed",
            "validation_message": "Answer generation was not successful."
        }

    return {
        "validation_status": "passed",
        "validation_message": "Basic validation checks passed."
    }
