
import pandas as pd
import matplotlib.pyplot as plt
from auth import DB_PATH
import sqlite3
from collections import Counter


def load_dataframe() -> pd.DataFrame:
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query("SELECT * FROM tracks", conn)


def popularity_bar(title: str = "Track Popularity") -> None:
    df = load_dataframe().sort_values("popularity", ascending=False)
    plt.figure(figsize=(10, 6))
    plt.barh(df["name"].head(10), df["popularity"].head(10))
    plt.gca().invert_yaxis()
    plt.xlabel("Popularity (0-100)")
    plt.title(title)
    plt.tight_layout()
    plt.show()




def artist_bar_chart(n: int = 10, title: str = "Top Artists in Your Playlists") -> None:
    """Creates a bar chart of top artists based on track count in playlists."""
    df = load_dataframe()
    
    # Count number of tracks per artist
    artist_counts = Counter(df["artist"])
    top_artists = dict(artist_counts.most_common(n))
    
    plt.figure(figsize=(10, 6))
    plt.barh(list(top_artists.keys()), list(top_artists.values()))
    plt.gca().invert_yaxis()
    plt.xlabel("Number of Tracks")
    plt.title(title)
    plt.tight_layout()
    plt.show()


def time_range_bar_chart(sp, time_range: str = "medium_term", title: str = "Your Top Tracks") -> None:
    """Shows top tracks for a specific time range from Spotify API."""
    # Get the user's top tracks for the specified time range
    results = sp.current_user_top_tracks(time_range=time_range, limit=10)
    
    # Extract track names and their popularity
    track_names = [item['name'] for item in results['items']]
    popularity = [item['popularity'] for item in results['items']]
    
    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(track_names, popularity)
    plt.gca().invert_yaxis()  # Invert y-axis to show highest at top
    plt.xlabel("Popularity (0-100)")
    plt.title(title)
    plt.tight_layout()
    plt.show()

