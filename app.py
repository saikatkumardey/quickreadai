import streamlit as st
import utils
from streamlit.components.v1 import html

st.set_page_config(
    page_title=f"{utils.APP_NAME}: AI-generated book summary",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed",
)

from streamlit_extras.add_vertical_space import add_vertical_space


# Define your javascript
# my_js = """
# window.onload = function(){
# var footer = document.getElementsByTagName("footer");
# console.log(footer);
# footer[0].innerHTML = "Made with love, by <a href='https://twitter.com/deysaikatkumar'>Saikat</a>";
# }
# """

# my_js = """
# console.log(document.getElementsByTagName("footer"));
# """

# # Wrapt the javascript as html code
# my_html = f"<script>{my_js}</script>"


import pandas as pd

import ai

utils.local_css("style.css")


@st.cache
def get_data():
    df = pd.read_json("non_fiction_data.json")
    df.drop_duplicates(["title", "author"], inplace=True)
    df["title_author"] = df["title"] + " | " + df["author"]
    return df


df = get_data()
num_books = len(df)

st.title(f"📚 {utils.APP_NAME}")

# add_vertical_space(num_lines=3)

st.markdown("Skim through the core ideas of non-fiction books")

# with st.sidebar:
#     st.write(f"Total: {num_books} books")


st.markdown("### Select 👇🏽", unsafe_allow_html=True)
title_author = st.selectbox(
    "**Select the book 👇🏽**",
    df.title_author,
    help="Select a book from the list to generate summary",
    label_visibility="collapsed",
)
title, authors = [item.strip() for item in title_author.split("|")]


def output_section():

    output = st.session_state.get("output", {})
    if not output:
        return

    title = st.session_state.get("title") or output["title"]
    authors = st.session_state.get("authors") or output["authors"]

    st.markdown(
        f"""
    ## {title}

    <span id="author">**Author(s)**: {output['authors']}</span><br/>
    <span id="genre">**Genre**: {output['genre']}</span>
    """,
        unsafe_allow_html=True,
    )

    for section in output["sections"]:
        name = section["name"].upper()
        body = section["body"]
        with st.expander(name, expanded=True):
            if type(body) == list:
                if len(body) == 0:
                    st.markdown("...")
                if len(body) == 1:
                    st.markdown(body[0])
                else:
                    for li in body:
                        st.markdown(f" - {li}")
            else:
                st.markdown(body)


if st.button("Get Summary", type="primary"):
    st.session_state["title"] = title
    st.session_state["authors"] = authors
    with st.spinner(
        f"Please wait. Generating summary for **{title}** by {authors}..."
    ):
        try:
            st.session_state["output"] = ai.get_gpt_response(
                title=title, authors=authors
            )
        except Exception as ex:
            st.error("Error generating summary, please try later..")

add_vertical_space(1)
output_section()

_, mid, _ = st.columns([1, 3, 1])

with mid:
    add_vertical_space(2)
    st.markdown(
        """<span id="twitter-link"> ❤️ Built by <a href="https://twitter.com/deysaikatkumar" target="_blank">Saikat Kumar Dey</a></span>""",
        unsafe_allow_html=True,
    )
