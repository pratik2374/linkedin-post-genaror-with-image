import streamlit as st
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
from llm_helper import llm

# Load environment variables
load_dotenv()
hf_token = os.getenv("HF_TOKEN")

# Hugging Face model configurations
flux = "black-forest-labs/FLUX.1-dev"

if not hf_token:
    raise ValueError("HF_TOKEN is not set. Please ensure it's defined in your .env file.")

# Initialize Hugging Face Inference Client
client = InferenceClient(model=flux, token=hf_token)


def generate_post_with_image(post, tag):
    # Generate the post
    query = llm.invoke(f"for the generated post give best suited prompt to make image for linkedin post and no preamble just given prompt in 1-2 line, prompt = {post}").content
    image = None

    # Generate an image if needed
    with st.spinner("Generating image... Please wait ⏳"):
        try:
            image = client.text_to_image(f"Illustration of {tag} and {query} in a professional LinkedIn style")
        except Exception as e:
            st.error(f"Error generating image: {e}")

    return image
