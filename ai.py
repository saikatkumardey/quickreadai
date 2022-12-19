import openai
from dotenv import load_dotenv
from prompt import prompt, template
import os
import json
import streamlit as st
import utils
from constants import *

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
GPT_MODEL = os.getenv("OPENAI_MODEL")

# TODO: remember to remove this while debugging
@st.cache(show_spinner=False, max_entries=CACHE_MAX_ENTRIES)
def get_gpt_response(title: str, authors: str, num_words: int = 100) -> dict:
    """
    This function takes in a title and authors for a book, and returns the generated text from the OpenAI GPT model.
    The generated text is a summary of the book with the given title and authors.

    Parameters:
    title (str): The title of the book
    authors (str): The authors of the book
    num_words (int, optional): The number of words to generate in the summary. Defaults to 100.

    Returns:
    dict: A dictionary containing the generated summary and other metadata.
    """
    # Format the prompt with the given title, authors, and number of words
    new_prompt_request = prompt.format(
        title=title,
        authors=authors,
        num_words=num_words,
    )
    # Add the template to the prompt
    new_prompt_request = f"""
    {new_prompt_request}
    {template}
    """
    # Make the request to the OpenAI GPT model
    response = openai.Completion.create(
        model=GPT_MODEL,
        prompt=new_prompt_request,
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return parse_gpt_response(response)


def parse_gpt_response(response: dict) -> dict:
    """
    This function takes in the response from the OpenAI GPT model and parses it to extract the generated summary.

    Parameters:
    response (dict): The response from the OpenAI GPT model.

    Returns:
    dict: A dictionary containing the generated summary and other metadata.
    """
    try:
        # Get the text of the response
        response = response["choices"][0]["text"]
        # Find the start and end indices of the summary in the response text
        response_start = response.find("{")
        response_end = response.rfind("}")
        # Get the summary from the response text
        response = response[response_start : response_end + 1]
        # Load the summary as a dictionary
        response_dict = json.loads(response)
        return response_dict
    except Exception as ex:
        print("error in parsing gpt response", ex)
        utils.dump_json(response)
        return {}
