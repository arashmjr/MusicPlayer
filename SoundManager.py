from typing import List
from SongModel import SongModel
from playsound import playsound
import pygame



class SoundManager:
    __instance = None
    songs: List[SongModel]
    current_song: SongModel = None
    current_index: int = None
    isPlaying: bool = None
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

        """ Virtually private constructor. """
        if SoundManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SoundManager.__instance = self


    def play_songs(self, songs: List[SongModel], index: int):
        self.songs = songs
        if index < len(songs) and index >= 0 :
            self.current_song = songs[index]
            self.current_index = index
            self.isPlaying = True
            print(self.__dict__)
            self.manager.music.load(self.current_song.url)
            self.manager.music.play()
            # playsound(self.current_song.url)
        return {'success': False}


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

    def unpause_song(self):
        if self.current_song is None:
            return
        self.isPlaying = True
        self.manager.music.unpause()

