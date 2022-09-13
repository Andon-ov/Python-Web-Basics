from django.shortcuts import render, redirect

from library.web_library.form import CreateProfileForm, AddBookForm, EditBookForm, DeleteProfileForm
from library.web_library.models import Book, Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    books = Book.objects.all()
    profile = get_profile()
    form = CreateProfileForm
    if not profile:
        return redirect('create profile page')

    context = {
        'profile': profile,
        'form': form,
        'books': books,
    }
    return render(request, 'home-with-profile.html', context)


def add_book_page(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = AddBookForm()
    context = {
        'form': form,
        'title': 'Create Modbus Device',
    }

    return render(request, 'add-book.html', context, )


def edit_book_page(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditBookForm(instance=book)
    context = {
        'form': form,
        'book': book
    }

    return render(request, 'edit-book.html', context)


def delete_book_page(request, pk):
    # OrderSparePart is the Model of which the object is present

    ob = Book.objects.get(pk=pk)
    ob.delete()
    return redirect('show index')  # for best results, redirect to the same page from where delete function is called


def book_details_page(request, pk):
    book = Book.objects.get(pk=pk)

    context = {
        'book': book
    }
    return render(request, 'book-details.html', context)


def profile_page(request):
    profile = get_profile()
    context = {
        'profile': profile
    }

    return render(request, 'profile.html', context)


def edit_profile_page(request, ):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'edit-profile.html', context)


def create_profile_page(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile_page(request):
    profile = get_profile()

    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile, )
        if form.is_valid():
            form.save()
        return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)
        context = {
            'form': form,
            'profile': profile
        }
    return render(request, 'delete-profile.html', context)


def base_page(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'base/base.html', context)
