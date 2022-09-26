from django.shortcuts import render, redirect

from petstagram.web.form import AddPhotoForm, EditPhotoForm
from petstagram.web.models import PetPhoto


def show_photo_details(request, pk):
    pet_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    # pet_photo = PetPhoto.objects.get(id=pk)

    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', context)


def like_photo_pet(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect(request, 'photo details', pk)


def add_photo_page(request):
    if request.method == 'POST':
        form = AddPhotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = AddPhotoForm()

    context = {
        'form': form
    }
    return render(request, 'photo_create.html', context)


def edit_photo_page(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditPhotoForm(instance=photo)
    context = {
        'form': form
    }
    return render(request, 'photo_edit.html', context)
