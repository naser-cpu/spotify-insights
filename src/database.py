"""
database.py
Lightweight SQLite helper layer for persisting track data.
"""

from __future__ import annotations
import sqlite3
from contextlib import contextmanager
from typing import Iterable, TypedDict
import auth  # Changed from relative import


class TrackRow(TypedDict):
    spotify_id: str
    name: str
    artist: str
    album: str
    popularity: int
    playlists: int  # Added playlists field


@contextmanager
def connect():
    """Context manager for database connections."""
    conn = sqlite3.connect(auth.DB_PATH)
    try:
        yield conn
    finally:
        conn.close()


def init() -> None:
    """Create the tracks table if it doesn't exist."""
    with connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tracks (
                spotify_id TEXT PRIMARY KEY,
                name       TEXT NOT NULL,
                artist     TEXT NOT NULL,
                album      TEXT,
                popularity INTEGER,
                playlists  INTEGER
            );
            """
        )
        conn.commit()


def insert(tracks: Iterable[TrackRow]) -> None:
    """Insert or update a batch of TrackRow dictionaries."""
    with connect() as conn:
        conn.executemany(
            """
            INSERT OR REPLACE INTO tracks
              (spotify_id, name, artist, album, popularity, playlists)
            VALUES
              (:spotify_id, :name, :artist, :album, :popularity, :playlists)
            """,
            tracks,
        )
        conn.commit()
