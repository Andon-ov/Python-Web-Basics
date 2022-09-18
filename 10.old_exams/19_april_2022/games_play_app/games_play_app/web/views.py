from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView

from games_play_app.web.form import CreateProfileForm, EditProfileForm
from games_play_app.web.models import ProfileModel


def get_profile():
    profile = ProfileModel.objects.all()
    if profile:
        return profile[0]
    return None


# Create your views here.
def show_index(request):
    return render(request, 'home-page.html')


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
    return render(request, 'create-profile.html', context)


def details_profile_page(request):
    full_name = ''
    profile = get_profile()

    if profile.first_name and profile.last_name:

        full_name = f"{profile.first_name} {profile.last_name}"
    context = {
        "profile": profile,
        "full_name": full_name,

    }
    return render(request, 'details-profile.html', context)


def edit_profile_page(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile_page(request):
    return render(request, 'delete-profile.html')


def dashboard_page(request):
    return render(request, 'dashboard.html')


def create_game_page(request):
    return render(request, 'create-game.html')


def details_game_page(request):
    return render(request, 'details-game.html')


def edit_game_page(request):
    return render(request, 'edit-game.html')


def delete_game_page(request):
    return render(request, 'delete-game.html')


# class CreateProfilePageView(CreateView):
#     fields = ('email', 'age', 'password')
#     model = ProfileModel
#     template_name = 'create-profile.html'
#     success_url = reverse_lazy('show index')



class DetailsProfilePageView(DetailView):
    fields = '__all__'
    model = ProfileModel
    template_name = 'details-profile.html'
    # success_url = reverse_lazy('show index')


# edit_profile_page
# delete_profile_page
# dashboard_page
# create_game_page
# details_game_page
# edit_game_page
# delete_game_page


def base_page(request):
    context = {
        'profile': get_profile()
    }
    return render(request, 'base/base.html', context)
