import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Safety Filter
def is_safe_query(query):
    unsafe_keywords = ["diagnose", "prescribe", "emergency", "life-threatening", "cure cancer"]
    return not any(keyword.lower() in query.lower() for keyword in unsafe_keywords)

# Chatbot Logic
def health_chatbot_response(query):
    if not is_safe_query(query):
        return "⚠️ I'm sorry, but I can't provide responses to critical medical inquiries. Please consult a healthcare professional."

    prompt = (
        "You are a helpful and friendly medical assistant. "
        "Provide general health information in simple words. "
        "Do not give medical diagnoses or treatment plans. "
        "Always advise consulting a doctor for serious issues.\n\n"
        f"User: {query}\n"
        "Assistant:"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].message['content'].strip()

# Streamlit UI
st.set_page_config(page_title="Health Chatbot", page_icon="🩺", layout="centered")

st.title("🩺 Health Chatbot Assistant")
st.write("Ask me general health-related questions. (Note: I'm not a doctor!)")

# Chat Input
user_input = st.text_input("Your Question:", key="user_input")

if st.button("Get Answer"):
    if user_input.strip() != "":
        with st.spinner("Thinking..."):
            response = health_chatbot_response(user_input)
        st.success("Here's what I found:")
        st.write(response)
    else:
        st.warning("Please enter a question.")

st.markdown("---")
st.caption("This chatbot provides general health information and does not replace professional medical advice.")
