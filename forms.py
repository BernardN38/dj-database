"""Forms for playlist app."""

from wtforms import StringField, SelectField, validators
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from models import db, Playlist,Song,PlaylistSong

BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist

class SongForm(ModelForm):
    class Meta:
        model = Song

class NewSongForPlaylistForm(FlaskForm):
    playlist = SelectField('Playlist Name', validators=[validators.Required()])
    song = SelectField('Song Name', validators=[validators.Required()])