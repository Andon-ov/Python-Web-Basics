from django.shortcuts import render

from petstagram.photos.models import Photo


def apply_user_liked_photo(photo):
    # TODO: fix this for current user when authentication is available
    photo.is_liked_by_user = photo.photolike_set.all()
    return photo


def index(request):
    photos = [apply_user_liked_photo(photo) for photo in Photo.objects.all()]
    context = {
        'photos': photos,
    }
    return render(request, 'common/home-page.html', context)
