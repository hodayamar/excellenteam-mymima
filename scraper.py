import re

from bs4 import BeautifulSoup
import requests

artists = []
songs = []

def get_artist_name(artist_page):

    url = artist_page
    page_response = requests.get(url, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")

    links = soup.find_all('table', attrs={'border': 0})

    for link in links:
        if link and link.text.strip():
            artists.append(link.text.strip())

def get_artist_songs(songs_page):

    url = songs_page
    page_response = requests.get(url, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")

    links = soup.find_all('table', attrs={'border': 0})

    for link in links:
        if link and link.text.strip():
            songs.append(link.text)


url = "https://www.mima.co.il/"
page_response = requests.get(url, timeout=5)
soup = BeautifulSoup(page_response.content, "html.parser")

links_of_artist = soup.find_all('a', attrs={'href': re.compile("^/?artist_letter")})
links_of_songs = soup.find_all('a', attrs={'href': re.compile("^/?song_letter")})

for link in links_of_artist:
    get_artist_name(url + link.get('href'))

for link in links_of_songs:
    get_artist_songs(url + link.get('href'))

print(artists[:10])

print(songs[:10])