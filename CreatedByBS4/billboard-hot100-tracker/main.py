import requests
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

date = input("YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=URL)
billboard_html = response.text

soup = BeautifulSoup(billboard_html, "html.parser")

title_tag = soup.find_all("div", class_="o-chart-results-list-row-container")

title_data = []
artists_data = []

for title in title_tag:
    # h3 태그에서 원하는 텍스트 가져오기
    title_text = title.find("h3", id="title-of-a-story").text.strip()
    title_data.append(title_text)

    # h3 태그의 다음 형제 태그 가져오기
    next_sibling = title.find("h3", id="title-of-a-story").find_next_sibling()

    # 다음 형제 태그에서 원하는 텍스트 가져오기
    if next_sibling:
        next_text = next_sibling.text.strip()
        if "Featuing" or "&" in next_text:
            next_text = re.sub(r'\bFeaturing\b|\b&\b', ',', next_text)
        artists_data.append(next_text)
    else:
        artists_data.append("N/A")

uri_list = []

for track_name, artist_name in zip(title_data, artists_data):
    results = sp.search(
        q=f"track:{track_name} artist:{artist_name}", type='track')
    if results['tracks']['items']:
        uri = results['tracks']['items'][0]['uri']
        uri_list.append(uri)

sp.playlist_replace_items(playlist_id="spotify:playlist:1gHloKPhVOc3YMIS9Vgnhv", items=uri_list)
