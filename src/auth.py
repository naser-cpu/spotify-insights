"""
auth.py
Handles Spotify authentication via Spotipy, drawing credentials
from .env-loaded config.py.
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from pathlib import Path
from dotenv import load_dotenv
import os

SCOPE = (
    "playlist-read-private playlist-read-collaborative "
    "user-library-read user-top-read"
)

# Load .env (only once, at import time)
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

# Now read the variables
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI", "http://127.0.0.1:8888/callback")

DB_PATH = os.getenv("SPOTIFY_DB_PATH", "spotify_tracks.db")

if not (CLIENT_ID and CLIENT_SECRET):
    raise RuntimeError(
        "Spotify credentials not found. "
        "Add them to .env as SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET."
    )



def get_client() -> spotipy.Spotify:
    """Return an authenticated Spotipy client with comprehensive playlist access."""
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE,
        )
    )

