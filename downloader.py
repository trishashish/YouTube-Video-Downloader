# Import Flask and the library to download YouTube videos
from flask import Flask, render_template, request
from pytube import YouTube

# Start the Flask app
app = Flask(__name__)

# Render the form
@app.route('/')
def renderForm():
    return render_template('index.html')

# Download the video
@app.route('/downloaded/', methods =["GET", "POST"])
def downloadVideo():
    # Ask the user what video they'd like to download
    video_link = request.form.get("link")
    yt = YouTube(video_link)

    # Download the video to the home folder
    yt.streams.filter(progressive=True)
    highest_res = yt.streams.get_highest_resolution()
    highest_res.download()

    return render_template('downloaded.html')