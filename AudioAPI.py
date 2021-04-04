from playsound import playsound
from flask_classy import FlaskView, route
from SoundManager import SoundManager
from SongModel import SongModel
from flask import Flask, render_template, request

class AudioApi(FlaskView):

    # @route('/play', methods=['POST'])
    # def play(self):
    #     SoundManager.get_instance().play_songs()
    #     return 'Success'
    #
    #
    # @route('/next', methods=['GET'])
    # def next(self):
    #     SoundManager.get_instance().next_song()
    #     return 'Success'
    #
    #
    # @route('/previous', methods=['GET'])
    # def previous(self):
    #     SoundManager.get_instance().previous_song()
    #     return 'Success'
    #
    # @route('/pause', methods=['GET'])
    # def pause(self):
    #     SoundManager.get_instance().pause_song()
    #     return 'Success'
    #
    # @route('/resume', methods=['GET'])
    # def resume(self):
    #     SoundManager.get_instance().resume_song()
    #     return 'Success'

    @route('/', methods=['GET'])
    def set(self):
        songs_list = [SongModel(id=50,
                                name="Tanha-Nazar",
                                artist="Sirvan khosravi",
                                genre="pop",
                                duration=150.5,
                                url=r"resources\song1.mp3"),
                      SongModel(id=51,
                                name="Khabam Ya Bidaram",
                                artist="Ebi",
                                genre="pop",
                                duration=150.5,
                                url=r"resources\song2.mp3"),
                      SongModel(id=52,
                                name="khatere",
                                artist="sirvan khosravi",
                                genre="pop",
                                duration=150.5,
                                url=r"resources\song3.mp3"),
                      SongModel(id=53,
                                name="kalaf",
                                artist="chavoshi",
                                genre="pop",
                                duration=150.5,
                                url=r"resources\song4.mp3"),
                      ]
        SoundManager.get_instance().set_songs(songs_list, 0)
        return render_template('index.html')




