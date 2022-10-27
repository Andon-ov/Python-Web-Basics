from django.shortcuts import render, redirect

from library.web_app.forms import BookCreateForm, BookEditeForm, BookDeleteForm, ProfileCreateForm, ProfileEditeForm, \
    ProfileDeleteForm
from library.web_app.models import Book, Profile


def get_profile():
    try:
        return Profile.objects.first()
    except Profile.DoesNotExist as ex:
        return None


def show_index(request):
    if get_profile() is None:
        return redirect('create profile')
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'common/home-with-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookCreateForm()
    context = {
        'form': form
    }
    return render(request, 'book/add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = BookEditeForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookEditeForm(instance=book)
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'book/edit-book.html', context)


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    form = BookDeleteForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect('home')


def show_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    context = {
        'book': book
    }
    return render(request, 'book/book-details.html', context)


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile/profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST, )
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileCreateForm()
    context = {
        'form': form
    }
    return render(request, 'profile/home-no-profile.html', context)


def edite_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileEditeForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileEditeForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileDeleteForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'profile/delete-profile.html', context)
