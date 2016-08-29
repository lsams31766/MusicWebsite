from django.db import models

class Song(models.Model):
   song_name = models.CharField(max_length=100)
   artist = models.CharField(max_length=100)
   genre = models.CharField(max_length=100)
   
   def __str__(self):
      return self.song_name

class SongFile(models.Model):
   song = models.ForeignKey(Song, on_delete=models.CASCADE)
   link_location = models.CharField(max_length=100)
   link_type = models.CharField(max_length=100)

   def __str__(self):
      return self.link_location