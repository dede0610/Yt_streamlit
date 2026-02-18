import os
import re
from datetime import datetime

from pytubefix import YouTube
import streamlit as st


def _safe_filename(name):
    # Windows-illegal characters: \ / : * ? " < > |
    name = re.sub(r'[\\/*?:"<>|]', "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name[:120]


def download(url, folder_path=os.getcwd()):
    """
    function that takes an URL and a folder path to download online youtube videos on your laptop locally
    return a dictionary object with title and date of downloading
    """

    yt = YouTube(url)
    print(f"Video title: {yt.title}")

    yd = yt.streams.get_highest_resolution()

    st.write(f"Downloading video: {yd.title}...")

    filename = _safe_filename(yd.title) + ".mp4"

    # Download video 
    yd.download(output_path=folder_path, filename=filename)
    st.success(f"Download is over ! 😀")

    return filename
