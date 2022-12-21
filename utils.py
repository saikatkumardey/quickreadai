import streamlit as st
import json
from constants import NOW


def dump_json(response, path="data/response.json"):

    with open(path, "w") as fp:
        json.dump(response, fp)


def dump_text(text):
    with open(f"data/prompt-{NOW}", "w") as fp:
        fp.write(text)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)
