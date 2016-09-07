from django.http import Http404
from django.http import HttpResponse
from .models import Song
from django.shortcuts import render
from dropbox_utility import GenerateAccessToken, GetFilesInDir, GetTextFileContent
import os

# Create your views here.
def index(request):
    #    all_songs = Song.objects.all()
    #    return render(request, 'Music/index.html',{'all_songs': all_songs})
    GenerateAccessToken() # make sure we can access Dropbox
    load_songs_to_db() # if no songs in database, load from import file
    #TODO - use cached db version of chords not Drop Box version
    # USING drop box chods directory
    #all_songs = GetFilesInDir('/chords/')
    #return render(request, 'Music/index.html',{'all_songs': all_songs})
    #
    #USING db for list
    all_songs = Song.objects.all()
    return render(request, 'Music/index.html',{'all_songs': all_songs})
    

def detail(request, song_id):
    #return HttpResponse('<h1>This is the detail for song ' + str(song_id) + '</h1>')
    try:
        song = Song.objects.get(pk=song_id)
        text_output = GetTextFileContent(song_id)
        print text_output
        #TODO put the text into a variable the page can see
    except Song.DoesNotExist:
        raise Http404('Song Does not Exist')
    return render(request, 'Music/detail.html', {'song': song, 'text_output' : text_output})

def show_file(request, song_file_name):
    print 'show_file got ' + song_file_name
    

def load_songs_to_db():
   if Song.objects.count() > 1:
       return #do not add from file list if already in db
    #use ../utiltities/songs_artists_lists.py to laod db with songs
   songs_file = '../utiltities/songs_artists_list.txt'
   songs_list = []
   default_artist = 'Unknown'
   cur_dir = os.getcwd()
   songs_file = os.path.join(cur_dir, songs_file)
   print 'working directory at ' + os.getcwd()
   print 'songs list at ' + songs_file
   with open(songs_file) as f:
      songs_list = f.readlines()
   for song in songs_list:
       try:
          song_split = song.split(',')
          song_file_name = song_split[0]
          # do not save part that is /Users/larrysamuels/Dropbox/
          pos = song_file_name.find('Dropbox/')
          if pos > 0:
              song_file_name = song_file_name[pos + 7:]
          song_name = song_split[1]
          if len(song_split) > 2:
              artist = song_split[2]
          else:
             artist = default_artist
          print song_file_name + ',' + song_name + ',' + artist + ',' + 'Rock'
          new_song = Song(file_name = song_file_name, song_name = song_name, artist = artist, genre = 'Rock')
          new_song.save()
       except:
          print 'error reading song into db'
   
