from django.test import TestCase
from facts.models import Artists, Facts, Songs


class FactsTestCase(TestCase):

    def setUp(self):
        Artists.objects.create(name="Three Days Grace")
        Artists.objects.create(name="Starset")
        Artists.objects.create(name="Amy Lee")
        Artists.objects.create(name="Red")
        Artists.objects.create(name="Apocalyptica")

        Songs.objects.create(name="One Too Many", artist=Artists.objects.get(name="Three Days Grace"))
        Songs.objects.create(name="It has began", artist=Artists.objects.get(name="Starset"))
        Songs.objects.create(name="Speak To Me", artist=Artists.objects.get(name="Amy Lee"))
        Songs.objects.create(name="Gone", artist=Artists.objects.get(name="Red"))
        Songs.objects.create(name="I Don't Care", artist=Artists.objects.get(name="Apocalyptica"))

        Facts.objects.create(author="Three Days Grace's member",
                             message="Three Days Grace's new album \"Human\" Available Now!",
                             song=Songs.objects.get(name="One Too Many"))
        Facts.objects.create(author="Starset's fan",
                             message="It's a good song!",
                             song=Songs.objects.get(name="It has began"))
        Facts.objects.create(author="SpongeBob",
                             message="What a song!!",
                             song=Songs.objects.get(name="Speak To Me"))
        Facts.objects.create(author="Red's fan",
                             message="What a song!!",
                             song=Songs.objects.get(name="Gone"))
        Facts.objects.create(author="Apocalyptica's fan",
                             message="What a song!!",
                             song=Songs.objects.get(name="I Don't Care"))

    def test_basic_model(self):

        three_days_grace = Artists.objects.get(name="Three Days Grace")
        one_too_many = Songs.objects.get(name="One Too Many")
        one_too_many_fact = Facts.objects.get(author="Three Days Grace's member")
        self.assertEqual(three_days_grace.artist_name(), "Three Days Grace")
        self.assertEqual(one_too_many.song_name(), "One Too Many")
        self.assertEqual(one_too_many_fact.get_fact(), "Three Days Grace's new album \"Human\" Available Now!")
