from pytube import YouTube
from datetime import datetime
import os

def Download(url):
    metadata = {}

    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    yd = yt.streams.get_highest_resolution()

    metadata = {'title': yd.title,
                'hour': datetime.now(),
                'date': datetime.now().strftime("%d-%m-%Y")
                }
    # Create Downloads folder if it doesn't already exist
    if not os.path.exists("../Downloads"):
        os.makedirs("../Downloads")


    # Download video to Downloads folder
    yd.download(os.path.join(os.getcwd(), "../Downloads"))

    return metadata
