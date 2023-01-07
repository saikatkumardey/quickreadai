import streamlit as st
import json


def dump_json(response, path="data/response.json"):
    """
    Dump the response to a json file.
    Args:
        response: the response to be dumped.
        path: the path to the file."""
    with open(path, "w") as fp:
        json.dump(response, fp)


def dump_text(text, path):
    """
    Write a text to a file.
    Args:
        text: text to write
        path: path to the file"""
    with open(path, "w") as fp:
        fp.write(text)


def local_css(path):
    """
    This function is used to load the local css file.

    Args:
        path: the path of the css file.

    Returns:
        None"""
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def remote_css(url):
    """
    This function is used to add a remote css file to the streamlit app.

    Args:
        url: the url of the css file

    Returns:
        None"""
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name):
    """
    This function is used to display icons in the streamlit app.

    Args:
        icon_name: The name of the icon to be displayed.

    Returns:
        None"""
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)
