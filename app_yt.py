import streamlit as st
from utils import Download

st.title('YouTube Downloader')
url = st.text_input(label='Enter an url:')
metadata = dict()

if url:
    folder_path = st.text_input(label='Enter the folder path in which you want the video to be downloaded:')
    if folder_path:
        st.write("Downloading...")
        metadata = Download(url, folder_path)
        st.success(f"Download of : {metadata['title']} is over ! 😀")

        with open('log.txt', 'a') as f:
            f.write(f"{metadata['time']}, Title : {metadata['title']} , {url}\n")

    else:
        st.write('No folder path')


#st.image('image/OIP.jpeg')



