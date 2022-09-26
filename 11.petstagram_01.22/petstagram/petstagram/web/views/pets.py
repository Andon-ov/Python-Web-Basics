from django.shortcuts import redirect, render

from petstagram.web.form import CreatePetForm, EditPetForm, DeletePetForm
from petstagram.web.models import Pet
from petstagram.web.views.helpers import get_profile


def pet_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    context = {
        'form': form,
        'pet': instance
    }
    return render(request, template_name, context)


def create_pet_page(request):
    return pet_action(request, CreatePetForm, 'show profile', Pet(user_profile=get_profile()), 'pet_create.html')


def edit_pet_page(request, pk):
    return pet_action(request, EditPetForm, 'show profile', Pet.objects.get(pk=pk), 'pet_edit.html')


def delete_pet_page(request, pk):
    return pet_action(request, DeletePetForm, 'show profile', Pet.objects.get(pk=pk), 'pet_delete.html')


#
# def add_pet_page(request):
#     if request.method == 'POST':
#         form = AddPetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('show index')
#     else:
#         form = AddPetForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'pet_create.html', context)


