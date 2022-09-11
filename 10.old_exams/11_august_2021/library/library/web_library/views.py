from django.shortcuts import render, redirect

from library.web_library.form import CreateProfileForm, AddBookForm, DeleteBookForm
from library.web_library.models import Book, Profile


# Create your views here.
def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = get_profile()
    form = CreateProfileForm
    if not profile:
        return redirect('create profile page')

    context = {
        'profile': profile,
        'form': form,
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
    }

    return render(request, 'add-book.html', context)


def edit_book_page(request, pk):
    book = Book.objects.get(pk=pk)
    # if request.method == 'POST':
    #     form = EditRecipeForm(request.POST, instance=recipe)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('show index')
    # else:
    #     form = EditRecipeForm(instance=recipe)
    context = {
        # 'form': form,
        'book': book
    }

    return render(request, 'edit-book.html', context)


def delete_book_page(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteBookForm(instance=book)
    context = {
        'form': form,
        'book': book
    }

    return render(request, 'delete-book.html', context)

def book_details_page(request, pk):
    book = Book.objects.get(pk=pk)
    # if request.method == 'POST':
        # form = EditRecipeForm(request.POST, instance=recipe)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('show index')
    # else:
    #     form = EditRecipeForm(instance=recipe)
    context = {
        # 'form': form,
        'book': book
    }
    return render(request, 'book-details.html', context)


def profile_page(request):
    return render(request, 'profile.html')


def edit_profile_page(request):
    return render(request, 'edit-profile.html')


def create_profile_page(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES, )
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
    return render(request, 'delete-profile.html')
