from django.shortcuts import render


# Create your views here.
def show_index(request):
    return render(request, 'home-with-profile.html')





def add_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
    return render(request, 'add-album.html')


def details_album(request, pk):
    return render(request, 'album-details.html')


def edit_album(request, pk):
    return render(request, 'edit-album.html')


def delete_album(request, pk):
    return render(request, 'delete-album.html')


def profile_details(request):
    return render(request, 'profile-details.html')


def profile_create(request):
    return render(request, 'home-no-profile.html')


def profile_delete(request):
    return render(request, 'profile-delete.html')
