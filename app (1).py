# app.py
import streamlit as st
from chatbot import chatbot_response

# Title of the app
st.title("GreenLife Foods Chatbot")
st.write("Welcome to GreenLife Foods! Ask about our products or place an order.")

# User input box
user_input = st.text_input("Type your message here:")

# Display the bot's response
if user_input:
    bot_response = chatbot_response(user_input)
    st.write(f"Bot: {bot_response}")