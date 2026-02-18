import os

from yt_download import download
import streamlit as st

st.title("YouTube Downloader")
url = st.text_input(label="Enter an url:")


def read_binary_file(filepath):
    with open(filepath, mode="rb") as f:
        data = f.read()
    return data


if url:
    try:
        folder_path = os.path.join(os.getcwd(), "downloads")
        filename = download(url, folder_path=folder_path)
        filepath = os.path.join(folder_path, filename)

        # Button to download on the client side
        st.download_button(
            label="Download video",
            data=read_binary_file(filepath),
            file_name=filename,
            mime="video/mp4",
        )

    except Exception as e:
        st.error(f"Error: {e}")
