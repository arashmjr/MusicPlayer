from playsound import playsound
from flask_classy import FlaskView, route
from SoundManager import SoundManager
from SongModel import SongModel

class AudioApi(FlaskView):

    @route('/play', methods=['POST'])
    def play(self):
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

        # print(len(songs_list))
        SoundManager.get_instance().play_songs(songs_list, 0)
        return 'Success'

    @route('/next', methods=['GET'])
    def next(self):
        SoundManager.get_instance().next_song()
        return 'Success'

    @route('/previous', methods=['GET'])
    def previous(self):
        SoundManager.get_instance().previous_song()
        return 'Success'

    @route('/pause', methods=['GET'])
    def pause(self):
        SoundManager.get_instance().pause_song()
        return 'Success'

    @route('/unpause', methods=['GET'])
    def unpause(self):
        SoundManager.get_instance().unpause_song()
        return 'Success'


