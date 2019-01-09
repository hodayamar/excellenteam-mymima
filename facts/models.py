from django.db import models


class Artists(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def artist_name(self):
        return self.name


class Songs(models.Model):

    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} by {self.artist}"

    def song_name(self):
        return self.name


class Facts(models.Model):

    author = models.CharField(max_length=200)
    message = models.TextField(blank=True, null=True)
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)

    def __str__(self):
        return f"[#{self.id}] by {self.author}"
