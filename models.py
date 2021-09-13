"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlists'
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    name = db.Column(
        db.Text,
        unique=True,
        nullable=False)

    description = db.Column(
        db.Text,
        nullable=True)
    songs = db.relationship('Song', secondary='playlist_songs', backref='playlists')

class Song(db.Model):
    """Song."""
    __tablename__ = 'songs'
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)
        
    title = db.Column(
        db.Text,
        unique=True,
        nullable=False)

    artist = db.Column(
        db.Text,
        nullable=False)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlist_songs'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    playlist = db.Column(
        db.Integer, 
        db.ForeignKey('playlists.id'),
        nullable=False)

    song = db.Column(
        db.Integer, 
        db.ForeignKey('songs.id'),
        nullable=False)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)