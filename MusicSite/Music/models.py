from django.db import models

class Song(models.Model):
   file_name = models.CharField(max_length=100)
   song_name = models.CharField(max_length=100)
   artist = models.CharField(max_length=100)
   genre = models.CharField(max_length=100)
   
   def __str__(self):
      return self.song_name  
  
class DropBoxAccount(models.Model):
    app_key = models.CharField(max_length=100)
    app_secret = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
    