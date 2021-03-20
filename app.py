from flask import Flask
from SoundManager import SoundManager
from SongModel import SongModel
# from flask_classy import FlaskView, route
from AudioAPI import AudioApi

app = Flask(__name__)

# SoundManager.get_instance().play_songs(songs_list, 0)
# SoundManager.get_instance().next_song()
# SoundManager.get_instance().next_song()
# SoundManager.get_instance().previous_song()
# SoundManager.get_instance().pause_song()

AudioApi.register(app, route_base='/')


if __name__ == '__main__':
    app.run()
