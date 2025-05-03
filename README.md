# Spotify Insights 🎧📊

**Spotify Insights** is a small Python CLI that explores your personal Spotify data, stores it in SQLite, and shows quick bar‑chart visualisations—all without leaving the terminal.

| Feature | Implementation |
|---------|---------------|
| **Lists your playlists** | Uses Spotify API to fetch your personal playlist collection |
| **Aggregates every track you own or follow** | Stores deduplicated tracks in SQLite database (`spotify_tracks.db`) |
| **Shows top artists & track popularity** | Generates interactive Matplotlib bar charts from your library data |
| **Displays your top tracks over time periods** | Analyzes listening history across short (4 weeks), medium (6 months), and long-term |
| **Clean database layer** | Direct SQLite integration without ORM overhead |

---

## ✨ Demo

```bash
$ python3 main.py
==================================================
                  Spotify Insights
==================================================

Options:
[1] List My Playlists
[2] Top Artists in My Playlists
[3] Top Popular Songs in My Playlists
[4] My Top Tracks by Time Period
[5] Exit
```


## 🗂 Project Structure

```bash
spotify-insights/
├── src/
│   └── spotify_insights/
│       ├── __init__.py
│       ├── auth.py          # OAuth or client‑credentials
│       ├── fetcher.py       # Spotify API calls
│       ├── database.py      # SQLite helper
│       ├── visualizer.py    # Matplotlib charts
│       └── main.py          # Interactive CLI
├── tests/                   # Pytest unit tests
├── .env                     # NOT committed – holds your secrets
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Quick Start

1. Clone & install

```bash
git clone https://github.com/<your‑handle>/spotify-insights.git
cd spotify-insights
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. Create a Spotify Developer App

Go to https://developer.spotify.com/dashboard

Create a new app → copy Client ID and Client Secret

Set a redirect URI: http://127.0.0.1:8888/callback

3. Add a .env

```dotenv
SPOTIPY_CLIENT_ID=YOUR_CLIENT_ID
SPOTIPY_CLIENT_SECRET=YOUR_CLIENT_SECRET
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
```

Add your .env and .venv/ to `.gitignore`.

4. Run

```bash
cd src
python3 main.py
```

The first run opens a browser for OAuth; approve once and a cached token is stored locally in .cache.


##  Requirements

spotipy 
matplotlib 
seaborn 
pandas
python-dotenv

All can be found in `requirements.txt`.

## Roadmap / Ideas

Here are some ideas you might want to try implementing:


- [ ] Release-year histogram to see your music taste by decade
- [ ] Genre distribution pie chart
- [ ] Dash/Plotly web dashboard for sharing insights



Have fun exploring your spotify data! If you implement any of these features or come up with your own cool ideas, feel free to contribute. The joy of personal projects is making them your own. 



