from typing import List
from SongModel import SongModel
# from playsound import playsound
import pygame



class SoundManager:
    __instance = None
    songs: List[SongModel]
    current_song: SongModel = None
    current_index: int = None
    isPlaying: bool = None
    isPaused: bool = None
    manager: pygame.mixer


    @staticmethod
    def get_instance():
        """ Static access method. """
        if SoundManager.__instance == None:
            SoundManager()
        return SoundManager.__instance

    def __init__(self):
        self.manager = pygame.mixer
        self.manager.init()
        self.songs = None
        self.current_index = None
        self.current_song = None
        self.isPlaying = None
        self.isPaused = None



        """ Virtually private constructor. """
        if SoundManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SoundManager.__instance = self

    def set_songs(self, songs: List[SongModel], index: int):
        self.songs = songs
        if index < len(songs) and index >= 0 :
            self.current_song = songs[index]
            self.current_index = index
            self.isPlaying = True
            # self.manager.music.load(self.current_song.url)
            # self.manager.music.play()
            # print(self.__dict__)
            # playsound(self.current_song.url)
        return {'success': False}

    def play_songs(self):
        print(self.current_song)
        self.manager.music.load(self.current_song.url)
        self.manager.music.play()
        self.isPaused = False


    def next_song(self):
        # self.manager.music.stop()
        # if len(self.songs) == 0:
        if self.songs is None:
            return
        self.current_index = self.current_index + 1
        if self.current_index >= len(self.songs):
            self.current_index = 0
        self.current_song = self.songs[self.current_index]
        self.isPlaying = True
        self.manager.music.load(self.current_song.url)
        self.manager.music.play()
        # playsound(self.current_song.url)


    def previous_song(self):
        # if len(self.songs) == 0:
        if self.songs is None:
            return
        self.current_index = self.current_index - 1
        if self.current_index < 0:
            self.current_index = len(self.songs) - 1
        self.current_song = self.songs[self.current_index]
        self.isPlaying = True
        self.manager.music.load(self.current_song.url)
        self.manager.music.play()
        # playsound(self.current_song.url)

    def pause_song(self):
        if self.current_song is None:
            return
        self.isPlaying = False
        self.manager.music.pause()
        self.isPaused = True


    def resume_song(self):
        if self.isPaused == True:
            self.manager.music.unpause()
        else:
            self.play_songs()

        self.isPaused = False


    # def resume_song(self):
    #     if self.current_song is None:
    #         return
    #     self.isPlaying = True
    #     self.manager.music.unpause()



