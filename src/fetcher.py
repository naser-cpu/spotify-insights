"""
fetcher.py – pull all tracks from every playlist you own / follow.
"""

from __future__ import annotations
from typing import List, TypedDict
from auth import get_client

class Track(TypedDict):
    spotify_id: str
    name: str
    artist: str
    album: str
    popularity: int
    playlists: int


def fetch_user_library(limit_per_playlist: int | None = None) -> List[Track]:
    """
    Grab tracks from every playlist the user owns or follows.
    If `limit_per_playlist` is given, cap the fetch per playlist.
    """
    sp = get_client()  # ← MUST be a SpotifyOAuth client, *not* ClientCredentials
    playlists = sp.current_user_playlists(limit=50)["items"]

    aggregate: dict[str, Track] = {}

    for pl in playlists:
        pl_id = pl["id"]
        offset = 0
        while True:
            # Use no `fields` filter (simplest) OR a valid one:
            # fields="items(track(id,name,artists,album,popularity))"
            items = sp.playlist_items(
                pl_id,
                limit=100,
                offset=offset,
            )

            if not items["items"]:
                break

            for it in items["items"]:
                t = it["track"]
                if t is None:          # local files can return None
                    continue

                tid = t["id"]
                entry = aggregate.setdefault(
                    tid,
                    {
                        "spotify_id": tid,
                        "name": t["name"],
                        "artist": t["artists"][0]["name"],
                        "album": t["album"]["name"],
                        "popularity": t["popularity"],
                        "playlists": 0,
                    },
                )
                entry["playlists"] += 1

            offset += 100
            if limit_per_playlist and offset >= limit_per_playlist:
                break

    return list(aggregate.values())
