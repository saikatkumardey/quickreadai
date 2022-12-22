import utils
from dotenv import load_dotenv
from deta import Deta
import os
from constants import *
import streamlit as st

load_dotenv()

deta = Deta(os.environ["DETA_KEY"])
summary_db = deta.Base(SUMMARY_DB)


def insert_summary(summary: dict) -> bool:
    """inserts summary into database.

    Args:
        summary: details of the non-fiction book including title,author,genre,core-idea etc.

    Returns:
        bool: whether insert was successful
    """
    if summary:
        try:
            summary_db.put(summary)
            return True
        except Exception as ex:
            print(f"[Deta] Error pushing summary to DB: {ex}")
            pass
    # TODO: use proper logging
    print("[Deta] can't insert empty summary")
    return False


@st.experimental_memo(show_spinner=False, max_entries=CACHE_MAX_ENTRIES)
def get_summary(title: str, authors: str) -> dict:
    """Gets summary from database based on title and authors.

    Args:
        title (str): title of the book
        authors (str): author names separated by commas

    Returns:
        dict: details of the non-fiction book including title,author,genre,core-idea etc.
    """
    try:
        data = summary_db.fetch({"title": title, "authors": authors}, limit=1)
        if data.count > 0:
            return data.items[0]
    except Exception as ex:
        print(f"[Deta] Error fetching summary from DB: {ex}")
    print("[Deta] no summary found")
    return {}
