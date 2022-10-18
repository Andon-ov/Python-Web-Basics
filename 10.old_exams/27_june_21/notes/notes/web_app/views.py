from django.shortcuts import render, redirect

from notes.web_app.form import EditNoteForm, CreateNoteForm, DeleteNoteForm, CreateProfileForm
from notes.web_app.models import Note, Profile


def has_profile():
    try:
        profile = Profile.objects.all()[0]
        return profile
    except IndexError:
        return None


def show_index(request):
    profile = has_profile()
    if not profile:
        return redirect('create profile')

    notes = Note.objects.all()
    contex = {
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', contex)


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST, )
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateNoteForm()
    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
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
            return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)
    context = {
        'form': form,
    }
    return render(request, 'note-delete.html', context)


def show_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)


def show_profile(request):
    profile = has_profile()
    if not profile:
        return redirect('create profile')
    note = Note.objects.count()

    context = {
        'profile': profile,
        'note': note,
    }
    return render(request, 'profile.html', context)


def add_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = has_profile()
    profile.delete()
    Note.objects.all().delete()
    return redirect('home')
