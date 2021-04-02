from flask import Flask, render_template, request
from SoundManager import SoundManager
from SongModel import SongModel
# from flask_classy import FlaskView, route
from AudioAPI import AudioApi

app = Flask(__name__)

AudioApi.register(app, route_base='/')

if __name__ == '__main__':
    app.run()
