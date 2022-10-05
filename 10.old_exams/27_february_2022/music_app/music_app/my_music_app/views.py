from django.shortcuts import render, redirect

from music_app.my_music_app.forms import CreatAlbumForm, EditAlbumForm, DeleteAlbumForm, CreatProfileForm, \
    DeleteProfileForm
from music_app.my_music_app.models import Album, Profile


def show_index(request):
    albums = Album.objects.all()
    context = {
        'albums': albums
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = CreatAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreatAlbumForm()
    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditAlbumForm(instance=album)
    context = {
        'form': form,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteAlbumForm(instance=album)
    context = {
        'form': form
    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = Profile.objects.all()[0]
    context = {
        'profile': profile
    }
    return render(request, 'profile-details.html', context)


def profile_create(request):
    profile = Profile.objects.all()[0]
    if request.method == 'POST':
        form = CreatProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = CreatProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.all()[0]
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = CreatProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'profile-delete.html', context)
