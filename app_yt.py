import streamlit as st
from utils import Download

st.title('YouTube Downloader')
url = st.text_input(label='Enter an url:')
metadata = dict()

if url:
    while len(metadata) == 0:
        st.write("Downloading...")
        metadata = Download(url)
    else:
        st.write(f"Download of : {metadata['title']} is over ! 😀")

    with open('log.txt', 'a') as f:
        f.write(f"{metadata['time']}, Title : {metadata['title']}\n")


#st.image('image/OIP.jpeg')



