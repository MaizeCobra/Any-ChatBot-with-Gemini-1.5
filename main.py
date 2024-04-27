import google.generativeai as genai
import streamlit as st
import os 
from dotenv import load_dotenv
load_dotenv()
from langchain.prompts import PromptTemplate

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

template = """You are a friendly and knowledgable fitness chatbot.
Answer questions within {number} words. Answer questions based on this chat's history..
Chat history(User): {User_history}
Chat history(Bot): {Bot_history}
Human: {user_input}
Bot: 
"""

prompt = PromptTemplate(input_variables=['user_input'], template = template)
model = genai.GenerativeModel("gemini-1.5-pro-latest")
chat = model.start_chat(history=[])
question = "initializer"

st.set_page_config("literally ANYTHING", "🤖", "wide", "auto")

st.header("literally ANYTHING")

if "User" not in st.session_state:
    st.session_state['User'] = []

if "Bot" not in st.session_state:
    st.session_state['Bot'] = []

question = st.text_input("Ask a question")
submit = st.button("Send")

if submit and question:
    response = chat.send_message(prompt.format(user_input=question, User_history=st.session_state['User'], Bot_history=st.session_state['Bot'], number=50))
    st.session_state['User'].append(question)
    st.session_state['Bot'].append(response.text)
    st.subheader("Bot:")
    st.write(response.text)

st.subheader("Chat History:")
for i in range(len(st.session_state['User'])):
    st.subheader("User:")
    st.write(st.session_state['User'][i])
    st.subheader("Bot:")
    st.write(st.session_state['Bot'][i])


