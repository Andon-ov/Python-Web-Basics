from django.shortcuts import render, redirect

from car_collection_app.web_app.forms import CarCreateForm, CarEditeForm, CarDeleteForm, ProfileCreateForm, \
    ProfileEditeForm, ProfileDeleteForm
from car_collection_app.web_app.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.first()
    except Profile.DoesNotExist as ex:
        return None


def show_index(request):
    return render(request, 'core/index.html')


def show_catalogue(request):
    cars = Car.objects.all()

    context = {
        'cars': cars,
    }
    return render(request, 'core/catalogue.html', context)


def create_car(request):
    if request.method == 'POST':
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'car/car-create.html', context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = CarEditeForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarEditeForm(instance=car)
    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarDeleteForm(instance=car)
    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car/car-delete.html', context)


def show_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'car': car,
    }
    return render(request, 'car/car-details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    else:
        form = ProfileCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'profile/profile-create.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileEditeForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')

    else:
        form = ProfileEditeForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ProfileDeleteForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile/profile-delete.html', context)


def show_profile(request):
    cars = Car.objects.all()
    profile = get_profile()
    total_price = sum([x.price for x in cars])
    context = {
        'profile': profile,
        'total_price': total_price,
    }
    return render(request, 'profile/profile-details.html', context)
