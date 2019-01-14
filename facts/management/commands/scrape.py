from django.core.management.base import BaseCommand
import re
from bs4 import BeautifulSoup
import requests

from facts.models import Songs, Facts, Artists


facts_re = re.compile("#CCFFCC|#EDF3FE")


def get_artist_pages(artist_page, home_url):
    url = artist_page
    page_response = requests.get(url, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")

    links = soup.find_all('table', attrs={'border': 0})

    for link in links:
        print("***********")
        artists = link.find_all('a', attrs={'href': re.compile("^/?artist_page")})

        for artist in artists:
            tmp_a = Artists.objects.create(name=artist.text)
            tmp_a.save()

            songs_of_artist = artist["href"]
            songs_url = home_url + songs_of_artist
            songs_response = requests.get(songs_url, timeout=5)
            songs_soup = BeautifulSoup(songs_response.content, "html.parser")

            songs = songs_soup.find_all('a', attrs={'href': re.compile("^/?fact_page")})
            for s in songs:
                tmp_s = Songs.objects.create(name=s.text, artist=tmp_a)
                tmp_s.save()
                facts_of_songs = s["href"]
                facts_url = home_url + facts_of_songs

                facts_response = requests.get(facts_url, timeout=5)
                facts_soup = BeautifulSoup(facts_response.content, "html.parser")

                facts = facts_soup.find_all('tr', attrs={'bgcolor': facts_re})

                for fact in facts:
                    tmp = fact.find("font").text if fact.find("font") else " "
                    txt = ''.join(list(fact.text[:-len(list(tmp))])) if tmp else ''.join(list(fact.text))
                    print(txt)
                    Facts.objects.create(author=tmp,
                                         message=txt,
                                         song=tmp_s)
def extract_data():

    url = "https://www.mima.co.il/"
    page_response = requests.get(url, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")

    links_of_artist = soup.find_all('a', attrs={'href': re.compile("^/?artist_letter")})

    for link in links_of_artist:
        get_artist_pages(url + link.get('href'), url)


def extract_data():

    url = "https://www.mima.co.il/"
    page_response = requests.get(url, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")

    links_of_artist = soup.find_all('a', attrs={'href': re.compile("^/?artist_letter")})

    for link in links_of_artist:
        get_artist_pages(url + link.get('href'),  url)


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):

        Artists.objects.all().delete()
        Facts.objects.all().delete()
        Songs.objects.all().delete()
        extract_data()


