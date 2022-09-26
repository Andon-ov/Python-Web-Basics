from django.shortcuts import render, redirect

from petstagram.web.form import CreatProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.web.models import PetPhoto, Pet, Profile
from petstagram.web.views.helpers import get_profile


def show_profile(request):
    profile = get_profile()

    pets = list(Pet.objects.filter(user_profile=profile))
    pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
    total_likes_count = sum(pp.likes for pp in pet_photos)
    total_pet_photos_count = len(pet_photos)

    context = {
        'profile': profile,
        'total_likes_count': total_likes_count,
        'total_pet_photos_count': total_pet_photos_count,
        'pets': pets
    }
    return render(request, 'profile_details.html', context)


def profile_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def create_profile_page(request):
    return profile_action(request, CreatProfileForm, 'show index', Profile(), 'profile_create.html')


def edit_profile_page(request):
    return profile_action(request, EditProfileForm, 'show profile', get_profile(), 'profile_edit.html')


def delete_profile_page(request):
    return profile_action(request, DeleteProfileForm, 'show index', get_profile(), 'profile_delete.html')

# def create_profile_page(request):
#     if request.method == 'POST':
#         form = CreatProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('show index')
#     else:
#         form = CreatProfileForm()
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'profile_create.html', context)
#
#
# def edit_profile_page(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('show profile')
#     else:
#         form = EditProfileForm(instance=profile)
#     context = {
#         'form': form,
#     }
#     return render(request, 'profile_edit.html', context)
