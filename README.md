# Download YouTube videos

Simple Streamlit web app to allow a user to download YouTube videos on their local machine based on the URL.

## Stack
The app is built in python: 
- Streamlit for the front-end
- Pytube API for the back-end



# Set up

## Prerequisites
To use this project, you will need:
* [Python 3.12](https://www.python.org/downloads/windows/)
* [git](https://git-scm.com/)
  
## How to run the project
To run the Youtube Downloader run:
```sh
git clone https://github.com/dede0610/Yt_streamlit.git
``` 
Navigate to the project folder:
```sh
cd Youtube_Downloader
``` 
Create a virtual environment:
```sh
python -m venv venv
```
Then activate the environment (windows):
```sh
.venv\Scripts\Activate.ps1
``` 
Install all the dependencies to run the project:
```sh
pip install -r requirements.txt
```  
Launch the app:
```sh
streamlit run app.py
``` 
Your web browser should open the streamlit interface from where you can enter the Youtube URL of the video to be downloaded.
