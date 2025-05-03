"""
main.py
Command-line entry point for Spotify Insights.
This script provides a menu-driven interface for users to interact with their Spotify data.
"""
from __future__ import annotations

import os
from auth import get_client, DB_PATH  # only to show DB path at the end
import database as db
import fetcher
from visualizer import popularity_bar, artist_bar_chart, time_range_bar_chart
from utils import clear_screen, exit_program


def load_data() -> None:
    """Fetch and store data from Spotify into the local database."""
    print("Loading your Spotify data...")
    tracks = fetcher.fetch_user_library()
    db.insert(tracks)
    print(f"Loaded {len(tracks)} tracks into the database.")


# ── Main Menu ───────────────────────────────────────────────────────────────────
def main_menu() -> None:
    """Main menu for Spotify Insights application."""
    db.init()  # Ensure DB and table exist
    
    # Load data only if database file doesn't exist(saves time)
    if not os.path.exists(DB_PATH):
        print("Database not found. Loading initial data...")
        try:
            load_data()
        except Exception as e:
            print(f"Error loading initial data: {e}")
            input("Press Enter to continue...")
    
    while True:
        # Main menu header
        title = "Spotify Insights"
        clear_screen()
        print('=' * 50)
        print(f'{title:^50}')
        print('=' * 50)
        print()

        # Menu options
        print("Options:")
        print("[1] List My Playlists")
        print("[2] Top Artists in My Playlists")
        print("[3] Top Popular Songs in My Playlists")
        print("[4] My Top Tracks by Time Period (4 weeks, 6 months, all time)")
        print("[5] Refresh Library Data")
        print("[6] Exit")

        choice = input("Select an option: ").strip()
        
        if choice == "1":
            list_playlists()
        elif choice == "2":
            show_top_artists()
        elif choice == "3":
            show_top_popularity()
        elif choice == "4":
            show_top_tracks_by_time()
        elif choice == "5":
            refresh_data()
        elif choice == "6":
            exit_program(None)
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


def refresh_data() -> None:
    """Manually refresh the local database with Spotify data."""
    clear_screen()
    print("Refreshing Spotify library data...")
    try:
        load_data()
        print("Data refresh complete!")
    except Exception as e:
        print(f"Error refreshing data: {e}")
    input("\nPress Enter to continue...")


# ── Helpers ───────────────────────────────────────────────────────────────────
def list_playlists() -> None:
    """Print all playlists the current user owns or follows."""
    sp = get_client()
    items = sp.current_user_playlists(limit=50)["items"]
    if not items:
        print("No playlists found on this account.")
        return

    print(f"{'PLAYLIST NAME':<40}  PLAYLIST ID")
    print("-" * 60)
    for pl in items:
        print(f"{pl['name']:<40}  {pl['id']}")
    
    input("\nPress Enter to continue...")




def show_top_artists() -> None:
    """Visualize top artists in your playlists."""
    clear_screen()
    print("Analyzing top artists in your playlists...")
    # First ensure we have the data
    tracks = fetcher.fetch_user_library()
    db.insert(tracks)
    artist_bar_chart(10)  # Show top 10 artists
    
    input("\nPress Enter to continue...")


def show_top_popularity() -> None:
    """Show tracks with highest popularity scores."""
    clear_screen()
    print("Showing your most popular tracks...")
    # First ensure we have the data
    tracks = fetcher.fetch_user_library()
    db.insert(tracks)
    popularity_bar("Your Top Tracks by Popularity")
    
    input("\nPress Enter to continue...")


def show_top_tracks_by_time() -> None:
    """Submenu for showing top tracks by time period."""
    while True:
        clear_screen()
        print('=' * 50)
        print(f'{"Select Time Period":^50}')
        print('=' * 50)
        print()
        
        print("Time Period Options:")
        print("[1] Last 4 weeks (short_term)")
        print("[2] Last 6 months (medium_term)")
        print("[3] All time (long_term)")
        print("[4] Return to main menu")
        
        choice = input("Select an option: ").strip()
        
        sp = get_client()
        
        if choice == "1":
            time_range_bar_chart(sp, "short_term", "Top Tracks - Last 4 Weeks")
            input("\nPress Enter to continue...")
        elif choice == "2":
            time_range_bar_chart(sp, "medium_term", "Top Tracks - Last 6 Months")
            input("\nPress Enter to continue...")
        elif choice == "3":
            time_range_bar_chart(sp, "long_term", "Top Tracks - All Time")
            input("\nPress Enter to continue...")
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")






if __name__ == "__main__":
    main_menu()