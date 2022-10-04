from django.shortcuts import render, redirect

from notes.web_notes.form import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm, DeleteProfileForm
from notes.web_notes.models import Note, Profile
from notes.web_notes.templatetags.tags import have_a_profile




def show_index(request):
    profile = have_a_profile()
    if not profile:
        return redirect('create profile')
    context = {
        'notes': Note.objects.all(),
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home-with-profile.html')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True
    }

    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.all()[0]
    notes = Note.objects.all()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            notes.delete()
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context)

# def cat_delete(request, pk):
#     cat = get_object_or_404(Cat, pk=pk)  # Get your current cat
#
#     if request.method == 'POST':         # If method is POST,
#         cat.delete()                     # delete the cat.
#         return redirect('/')             # Finally, redirect to the homepage.
#
#     return render(request, 'template_name.html', {'cat': cat})



def show_profile(request):
    context = {
        'profile': Profile.objects.all()[0],
        'all_notes': Note.objects.count()
    }
    return render(request, 'profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateNoteForm()
    context = {
        'form': form,
        'notes': Note.objects.all(),
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditNoteForm(instance=note)
    context = {
        'form': form,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteNoteForm(instance=note)
    context = {
        'form': form,
    }
    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)
