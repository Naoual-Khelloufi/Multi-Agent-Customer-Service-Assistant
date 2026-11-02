from typing import TypedDict, List, Any


class CustomerServiceState(TypedDict):
    question: str
    next_step: str
    supervisor_message: str
    context: str
    sources: List[str]
    retrieved_documents: List[Any]
    answer: str
    generation_status: str
    validation_status: str
    validation_message: str