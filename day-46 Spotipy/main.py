import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "YOUR CLIENT ID"
SPOTIPY_CLIENT_SECRET = "YOUR SECRET"
REDIRECT_URI = "https://www.google.com"
SCOPE = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://www.google.com",
        client_id= SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="fahri",
    )
)
user_id = sp.current_user()["id"]
# print(user_id)

date = input("Which year do you want to travel to ? Type the date in format YYYY-MM-DD")
playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard 100",
                                   public=False,
                                   description="this playlist made by my python code")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
bb_web_page = response.text

soup = BeautifulSoup(bb_web_page, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in song_names_spans]
# print(song_titles)

uri_codes = []

for song in song_titles:
    song_info = sp.search(f"{song} {date}", type="track")
    try:
        uri_code = song_info["tracks"]["items"][0]["uri"]
    except:
        print("this song is not available on spotify")
    else:
        uri_codes.append(uri_code)

sp.playlist_add_items(playlist_id=playlist["id"], items=uri_codes)
