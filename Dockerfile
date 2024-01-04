# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.8

# Create and change to the app directory.
WORKDIR /app

# Copy requirements.txt into the container.
COPY requirements.txt .

# Install any needed packages specified in requirements.txt.
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app.
COPY . .

# Make port 8501 available to the world outside this container.
EXPOSE 8501

# Run streamlit when the container launches.
CMD ["streamlit", "run", "app_yt.py"]
