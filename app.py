from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///capstone_spotify_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "up_the_planes"

os.environ['SPOTIPY_CLIENT_ID'] = '01480f8165f84e0f869d00a9cd62e934'
os.environ['SPOTIPY_CLIENT_SECRET'] = '9040ee998b904b7dbee1a62f229f8c6f'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:5000/playlists'

scope = "playlist-modify-public,playlist-modify-private,playlist-read-private,playlist-read-collaborative,user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route('/')
def root():
    """Homepage-placeholder"""

    return redirect('/playlists')

@app.route('/playlists')
def show_user_playlists():
    """Placeholder for now"""

    return(render_template('index.html'))