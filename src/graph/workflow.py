
from langgraph.graph import StateGraph, START, END
from src.graph.state import CustomerServiceState
from src.agents.supervisor_agent import supervisor_agent
from src.agents.retrieval_agent import retrieval_agent
from src.agents.answer_agent import answer_agent
from src.agents.validation_agent import validation_agent


# Route the question based on the Supervisor's decision
def route_question(state):
    return state["next_step"]


# Build the workflow
workflow = StateGraph(CustomerServiceState)

# Register agents as workflow nodes
workflow.add_node("supervisor", supervisor_agent)
workflow.add_node("retrieval", retrieval_agent)
workflow.add_node("answer", answer_agent)
workflow.add_node("validation", validation_agent)

# Define workflow connections
workflow.add_edge(START, "supervisor")

workflow.add_conditional_edges(
    "supervisor",
    route_question,
    {
        "retrieve": "retrieval",
        "end": END
    }
)

workflow.add_edge("retrieval", "answer")
workflow.add_edge("answer", "validation")
workflow.add_edge("validation", END)

# Compile the workflow
customer_service_app = workflow.compile()
