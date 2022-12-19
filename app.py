import streamlit as st
import utils

st.set_page_config(
    page_title=f"{utils.APP_NAME}: AI-generated book summary",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed",
)

from streamlit_extras.add_vertical_space import add_vertical_space
import pandas as pd
import ai

utils.local_css("static/style.css")


def get_data():
    """Returns book data from JSON file as Pandas DataFrame.

    Returns:
        df (pandas.DataFrame): DataFrame of book data.
    """
    df = pd.read_json("non_fiction_data.json")
    df.drop_duplicates(["title", "author"], inplace=True)
    df["title_author"] = df["title"] + " | " + df["author"]
    return df


def output_section():
    """Displays summary output."""
    output = st.session_state.get("output", {})
    if not output:
        return

    title = st.session_state.get("title") or output["title"]
    authors = st.session_state.get("authors") or output["authors"]
    genre = output["genre"]

    add_vertical_space(1)

    st.markdown(
        f"""
    ## {title}
    <span id="author">**Author(s)**: {authors}</span><br/>
    <span id="genre">**Genre**: {genre}</span>
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


def add_footer():
    """Add footer"""
    _, mid, _ = st.columns([1, 3, 1])
    with mid:
        add_vertical_space(2)
        st.markdown(
            """<span id="twitter-link"> ❤️ Built by <a href="https://twitter.com/deysaikatkumar" target="_blank">Saikat Kumar Dey</a></span>""",
            unsafe_allow_html=True,
        )


def main():
    df = get_data()

    st.title(f"📚 {utils.APP_NAME}")
    st.markdown(
        "Skim through the core ideas of non-fiction books in 2 minutes."
    )
    add_vertical_space(1)
    title_author = st.selectbox(
        "**Select the book 👇🏽**",
        df.title_author,
        help="Select a book from the list to generate summary",
        label_visibility="collapsed",
    )
    title, authors = [item.strip() for item in title_author.split("|")]

    if st.button("Get Summary", type="primary"):
        st.session_state["title"] = title
        st.session_state["authors"] = authors
        with st.spinner(
            f"Please wait. Getting summary for **{title}** by {authors}..."
        ):
            try:
                st.session_state["output"] = ai.get_gpt_response(
                    title=title, authors=authors
                )
            except Exception as ex:
                st.error("Error generating summary, please try later..")

    output_section()
    add_footer()


if __name__ == "__main__":
    main()
