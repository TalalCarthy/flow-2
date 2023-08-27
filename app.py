import os
import tempfile
import streamlit as st
from dotenv import load_dotenv

# config API stuff
try:
    load_dotenv('.env')
    api_key = os.getenv("OPENAI_API_KEY")
    langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
    langchain_project = os.getenv("LANGCHAIN_PROJECT")
    langchain_tracing = os.getenv("LANGCHAIN_TRACING_V2")
    langchain_endpoint = os.getenv("LANGCHAIN_ENDPOINT")

    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
        os.environ["LANGCHAIN_PROJECT"] = langchain_project
        os.environ["LANGCHAIN_TRACING_V2"] = langchain_tracing
        os.environ["LANGCHAIN_ENDPOINT"] = langchain_endpoint
    else:
        print("API key not found in environment variable or .env file.")
except FileNotFoundError:
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    else:
        print("API key not found in environment variable or .env file.")
