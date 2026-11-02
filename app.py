
import streamlit as st

from src.graph.workflow import customer_service_app


# Page configuration
st.set_page_config(
    page_title="Customer Service AI Assistant",
    page_icon="",
    layout="centered"
)

# Application title
st.title("Customer Service AI Assistant")
st.caption("AI-powered assistant for customer service agents")

st.divider()

# User question
question = st.text_area(
    "Enter your question:",
    placeholder="Example: How should an agent handle an angry customer?",
    height=100
)

# Generate answer
if st.button("Generate Answer", type="primary"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("Processing your question..."):

            try:
                result = customer_service_app.invoke({
                    "question": question
                })

                answer = result.get("answer", "")

                st.subheader("Generated Answer")

                if answer:
                    st.markdown(answer)
                else:
                    st.warning("No answer could be generated.")

            except Exception as error:
                st.error("An error occurred while processing your question.")
                print(f"Application error: {error}")
