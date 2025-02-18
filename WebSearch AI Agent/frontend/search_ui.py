import streamlit as st

import sys
import os
# Get the root directory of your project
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)

from agent.search_agent import search_with_agent  # Import the search agent

# Set Streamlit page config
st.set_page_config(page_title="Web Search AI Agent", page_icon="🔍", layout="wide")

# UI Layout
st.title("🔍 AI-Powered Web Search")

# User input box for search query
query = st.text_input("Enter your search query:")

# Button to trigger the search
if st.button("Search"):
    if query.strip():
        st.write("🔎 **Searching... Please wait.**")
        
        # Call the AI-powered agent with the user's query
        summary = search_with_agent(query)
        
        # Display the AI-generated summary below the input box
        st.subheader("📌 AI-Generated Summary:")
        st.write(summary)
    else:
        st.warning("Please enter a search query.")
