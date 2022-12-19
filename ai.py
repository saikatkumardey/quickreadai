import openai
from dotenv import load_dotenv
from prompt import prompt, template
import os
import json
import streamlit as st
import utils

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
GPT_MODEL = os.getenv("OPENAI_MODEL")

# TODO: remember to remove this while debugging
@st.cache(show_spinner=False, persist=True, max_entries=100)
def get_gpt_response(title, authors, num_words=100):
    new_prompt_request = prompt.format(
        title=title,
        authors=authors,
        num_words=num_words,
    )
    new_prompt_request = f"""
    {new_prompt_request}
    {template}
    """
    print(new_prompt_request)
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


def parse_gpt_response(response):
    try:
        response = response["choices"][0]["text"]
        response_start = response.find("{")
        response_end = response.rfind("}")
        response = response[response_start : response_end + 1]
        print(response)
        response_dict = json.loads(response)
        return response_dict
    except Exception as ex:
        print("error in parsing gpt response", ex)
        utils.dump_json(response)
        return {}
