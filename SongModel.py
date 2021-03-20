class SongModel:
    name: str
    artist: str
    genre: str
    url: str
    id: int
    duration: float


    def __init__(self, id: int, name: str, artist: str, genre: str, url: str, duration: float):

        self.id = id
        self.name = name
        self.artist = artist
        self.genre = genre
        self.url = url
        self.duration = duration
