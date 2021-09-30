from app import db

# Tabla Song
class Song(db.Model):
    __tablename__ = 'Song'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    artist = db.Column(db.String)
    genre = db.Column(db.String)
    album = db.Column(db.String, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    link = db.Column(db.String, unique=True)

    def __init__(self, name, artist, genre, album, year, link):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.album = album
        self.year = year
        self.link = link

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    fecha = db.Column(db.Date)
    genre = db.Column(db.String)

    def __init__(self, email, password, fecha, genre):
        self.email = email
        self.password = password
        self.fecha = fecha
        self.genre = genre

class FavoriteSong(db.Model):
    __tablename__ = 'FavoriteSong'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.ForeignKey("User.id"))
    song_id = db.Column(db.ForeignKey("Song.id"))

class Room(db.Model):
    __tablename__ = 'Room'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String, unique=True)
    user_id = db.Column(db.ForeignKey("User.id"))
    song_id = db.Column(db.ForeignKey("Song.id"), nullable=True)

    def __init__(self, code, user_id, song_id):
        self.code = code
        self.user_id = user_id
        self.song_id = song_id
