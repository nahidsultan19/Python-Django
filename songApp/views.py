from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Songs
from .forms import SongsForm

from .filters import SongsFilter


def Song(request, pk=0):
    context = {
        # 'songs': Songs.objects.all(),
        'form': SongsForm()
    }

    # if request.method == 'POST':
    #     song = SongsForm(request.POST)
    #     if song.is_valid():
    #         song.save()
    #     return redirect('list')
    # return render(request, 'index.html', context)

    if request.method == 'GET':
        # code for update song
        if pk == 0:
            form = SongsForm()
        else:
            songs = Songs.objects.get(id=pk)
            form = SongsForm(instance=songs)
        return render(request, 'index.html',  {'form': form})
    else:
        if pk == 0:
            form = SongsForm(request.POST)
        else:
            songs = Songs.objects.get(id=pk)
            form = SongsForm(request.POST, instance=songs)
        if form.is_valid():
            form.save()
        return redirect('song_list')


def List(request):
    song_list = Songs.objects.all()

    # item filter
    myFilter = SongsFilter(request.GET, queryset=song_list)
    song_list = myFilter.qs
    context = {
        'song_list': song_list,
        'myFilter': myFilter
    }
    return render(request, 'song_list.html', context)


def Delete_song(request, pk):
    songs = Songs.objects.get(id=pk)
    if request.method == 'POST':
        songs.delete()
        return redirect('song_list')
    context = {'songs': songs}
    return render(request, 'delete_song.html', context)
