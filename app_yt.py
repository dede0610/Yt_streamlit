import os

import streamlit as st
from yt_download import download

st.title("YouTube Downloader")
url = st.text_input(label="Enter an url:")
metadata = dict()

def read_binary_file(filepath):
    with open(filepath, mode='rb') as f:
        data = f.read()
    return data

if url:
    try:
        filename = download(url)
        
        #with open("log.txt", "a") as f:
        #    f.write(f"{metadata['time']}, Title : {metadata['title']} , {url}\n")

        filepath = os.path.join(os.getcwd(), filename)

        # Button to download on the client side
        st.download_button(label="Download video", data=read_binary_file(filepath), file_name=filename, mime='video/mp4') 

    except Exception as e:
        print(e)
