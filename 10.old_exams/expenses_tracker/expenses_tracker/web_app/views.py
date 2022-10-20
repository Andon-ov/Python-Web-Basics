from django.shortcuts import render, redirect

from expenses_tracker.core.prifile_utils import has_profile
from expenses_tracker.web_app.forms import CreateProfileForm, EditeProfileForm, CreateExpenseForm, \
    EditeExpenseForm, DeleteExpenseForm, DeleteProfileForm
from expenses_tracker.web_app.models import Expense


def show_index(request):
    profile = has_profile()
    if profile is None:
        return redirect('create profile')

    expenses = Expense.objects.all()

    context = {
        'profile': profile,
        'expenses': expenses,
    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateExpenseForm()
    context = {
        'form': form
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditeExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditeExpenseForm(instance=expense)
    context = {
        'form': form
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteExpenseForm(instance=expense)
    context = {
        'form': form
    }
    return render(request, 'expense-delete.html', context)


# Profile views


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()
    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = has_profile()
    if request.method == 'POST':
        form = EditeProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditeProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = has_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('create profile')

    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)


def show_profile(request):
    profile = has_profile()
    expenses_count = Expense.objects.count()

    context = {
        'profile': profile,
        'expenses_count': expenses_count,

    }
    return render(request, 'profile.html', context)

# def delete_profile(request):
#     profile = has_profile()
#
#     if request.method == 'POST':
#         profile.delete()
#         profile.profile_image.close()
#         profile.profile_image.delete()
#         Expense.objects.all().delete()
#
#         return redirect('create profile')
#
#     return render(request, 'profile-delete.html')
