from django.http import Http404
from django.http import HttpResponse
from .models import Song
from django.shortcuts import render
from dropbox_utility import GenerateAccessToken, GetFilesInDir, GetTextFileContent

# Create your views here.
def index(request):
    #    all_songs = Song.objects.all()
    #    return render(request, 'Music/index.html',{'all_songs': all_songs})
    GenerateAccessToken() # make sure we can access Dropbox
    all_songs = GetFilesInDir('/chords/')
    return render(request, 'Music/index.html',{'all_songs': all_songs})

def detail(request, song_id):
    try:
        song = Song.objects.get(pk=song_id)
    except Song.DoesNotExist:
        raise Http404('Song Does not Exist')
    return render(request, 'Music/detail.html', {'song': song})




