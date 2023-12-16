import streamlit as st
from yt_download import download
import os

st.title("YouTube Downloader")
url = st.text_input(label="Enter an url:")
metadata = dict()
folder_path = os.getcwd() # We save the file in a specific folder on the server side


def read_binary_file(filepath):
    with open(filepath, mode='rb') as f:
        data = f.read()
    return data

if url:
    # folder_path = st.text_input(
    #     label="Enter the folder path in which you want the video to be downloaded:"
    # )
    # if folder_path:
    #     metadata = download(url, folder_path)
    #     st.success(f"Download of : {metadata['title']} is over ! 😀")

    #     with open("log.txt", "a") as f:
    #         f.write(f"{metadata['time']}, Title : {metadata['title']} , {url}\n")

    # else:
    #     st.write("No folder path")

    try:

        metadata = download(url, folder_path)
        st.success(f"Download of : {metadata['title']} is over ! 😀")
        with open("log.txt", "a") as f:
            f.write(f"{metadata['time']}, Title : {metadata['title']} , {url}\n")

        filepath = os.getcwd() + f"/videos_yt/{metadata['title']}" + ".mp4"

        st.download_button(label="Download video", data=read_binary_file(filepath),file_name=metadata['title'],mime='video/mp4') # Button to download on the client side

    except Exception as e:
        print(e)
        

# st.image('image/OIP.jpeg')
