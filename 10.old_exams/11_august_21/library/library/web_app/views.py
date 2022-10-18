from django.shortcuts import render, redirect

from library.web_app.form import CreateBookForm, EditBookForm, DeleteBookForm, CreateProfileForm, EditProfileForm, \
    DeleteProfileForm
from library.web_app.models import Book, Profile


def has_profile():
    try:
        return Profile.objects.all()[0]
    except IndexError:
        return None


def show_index(request):
    books = Book.objects.all()
    profile = has_profile()

    if not profile:
        return redirect('add profile')
    context = {
        'books': books,
    }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateBookForm()
    context = {
        'form': form,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditBookForm(instance=book)
    context = {
        'form': form,
    }
    return render(request, 'edit-book.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home page')


def show_book_details(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteBookForm(instance=book)
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'book-details.html', context)


def add_profile(request):
    profile = has_profile()
    if profile:
        return redirect('home page')
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = has_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


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
    return render(request, 'delete-profile.html', context)


def show_profile(request):
    profile = has_profile()
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)
