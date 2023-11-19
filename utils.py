import os

from pytube import YouTube
from datetime import datetime
import streamlit as st


def Download(url, folder_path):
    metadata = {}

    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    yd = yt.streams.get_highest_resolution()

    metadata = {'title': yd.title,
                'time': datetime.now()
                }

    if not os.path.isdir(folder_path):
        st.error('The provided folder does not exist. Please provide a valid folder path.')
        return

    file_path = os.path.join(folder_path, metadata['title'])

    # Download video to in the appropriate folder
    yd.download(file_path)

    return metadata

