from django.shortcuts import render, redirect

from music_app.web_app.form import EditAlbumForm, DeleteAlbumForm, CreatProfileForm, CreateAlbumForm, DeleteProfileForm
from music_app.web_app.models import Album, Profile


def has_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def show_index(request):
    profile = has_profile()
    if profile is None:
        return create_profile(request)

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
    album = Album.objects.filter(pk=pk).get()
    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditAlbumForm(instance=album)
    context = {
        'form': form,
        'album': album
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
        'form': form,
        'album': album,

    }
    return render(request, 'delete-album.html', context)


def create_profile(request):
    if has_profile() is not None:
        return redirect('home page')

    if request.method == 'POST':
        form = CreatProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreatProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = has_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)


def details_profile(request):
    profile = has_profile()
    all_albums = Album.objects.count()

    context = {
        'profile': profile,
        'all_albums': all_albums
    }
    return render(request, 'profile-details.html', context)
