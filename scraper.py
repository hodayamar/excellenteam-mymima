import re
from bs4 import BeautifulSoup
import requests
# from facts import models

artists = []
songs = []
all_facts = []
facts_re = re.compile("#CCFFCC|#EDF3FE")



def get_artist_name(artist_page):

    url = artist_page
    page_response = requests.get(url, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")

    links = soup.find_all('table', attrs={'border': 0})

    for link in links:
        if link and link.text.strip():
            artists.extend(link.text.strip().split("\n\xa0\xa0"))


def get_artist_songs(songs_page, home_url):
    url = songs_page
    page_response = requests.get(url, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")



    links = soup.find_all('table', attrs={'border': 0})

    for link in links:
        fcts = link.find_all('a', attrs={'href': re.compile("^/?fact_page")})
        print(fcts)
        for f in fcts:
            get_artist_facts(home_url + f.get('href'))
            print(home_url + f.get('href'))

        if link and link.text.strip():
            songs.extend(link.text.strip().split("\n\xa0\xa0"))


def get_artist_facts(song_url):

    page_response = requests.get(song_url, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    facts = page_content.find_all("tr", attrs={"bgcolor": facts_re})
    for fact in facts:
        # print(fact.text)
        all_facts.append({
            'text': fact.text,
            'publisher': fact.find("font").text if fact.find("font") else None
        })


def extract_data():

    url = "https://www.mima.co.il/"
    page_response = requests.get(url, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")

    links_of_artist = soup.find_all('a', attrs={'href': re.compile("^/?artist_letter")})
    links_of_songs = soup.find_all('a', attrs={'href': re.compile("^/?song_letter")})

    # for link in links_of_artist:
    #     get_artist_name(url + link.get('href'))

    for link in links_of_songs:
        get_artist_songs(url + link.get('href'), url)

    print(artists)
    print(all_facts)
    print(len(artists))

    print(len(songs))

# def insert_data_to_db():
#
#     [models.Artists.objects.create(name=artist) for artist in artists]
#
#     [models.Songs.objects.create(name=song) for song in songs]

extract_data()
# insert_data_to_db()
