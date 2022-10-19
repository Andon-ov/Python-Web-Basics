from django.shortcuts import render, redirect

from music_app.web_app.form import EditAlbumForm, DeleteAlbumForm, CreatProfileForm, CreateAlbumForm
from music_app.web_app.models import Album, Profile


def has_profile():
    profile = Profile.objects.all()
    try:
        return profile[0]
    except IndexError:
        return None


def show_index(request):
    profile = has_profile()
    if profile is None:
        return redirect('create profile')

    albums = Album.objects.all()

    context = {
        'albums': albums,

    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateAlbumForm()
    context = {
        'form': form
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditAlbumForm(instance=album)
    context = {
        'form': form
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteAlbumForm(instance=album)
    context = {
        'form': form
    }
    return render(request, 'delete-album.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreatProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreatProfileForm()
    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = has_profile()
    if request.method == 'POST':
        profile.delete()
        Album.objects.all().delete()
        return redirect('create profile')
    return render(request, 'profile-delete.html')


def details_profile(request):
    all_albums = Album.objects.count()

    profile = has_profile()
    context = {
        'profile': profile,
        'all_albums': all_albums
    }
    return render(request, 'profile-details.html', context)
