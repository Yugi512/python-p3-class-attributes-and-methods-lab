class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.song_increment()
        self.add_genres(self.genre)
        self.add_artist(self.artist)
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)


    @classmethod
    def song_increment(cls, increment = 1):
        cls.count += increment
    
    @classmethod
    def add_genres(cls,genre):
        cls.genres.append(genre)

        
    @classmethod
    def add_artist(cls,artist):
        cls.artists.append(artist)
        
    @classmethod
    def add_to_genre_count(cls,genre):
            if genre not in cls.genre_count:
                cls.genre_count[genre] = 1
                print(cls.genre_count)
            else:
                cls.genre_count[genre] +=1
                print(cls.genre_count)
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1

# breakpoint()