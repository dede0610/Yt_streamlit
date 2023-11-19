import os
from datetime import datetime

from pytube import YouTube
import streamlit as st


def download(url, folder_path):
    """
    function that takes an url and a forder paths to download youtube videos online on local on your pc
    return a dictionary object with title and date of downloading
    """

    metadata = {}

    st.write("Downloading...")

    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    yd = yt.streams.get_highest_resolution()

    metadata = {"title": yd.title, "time": datetime.now()}

    if not os.path.isdir(folder_path):
        st.error(
            "The provided folder does not exist. Please provide a valid folder path."
        )
        return

    file_path = os.path.join(folder_path, metadata["title"])

    # Download video to in the appropriate folder
    yd.download(file_path)

    return metadata
