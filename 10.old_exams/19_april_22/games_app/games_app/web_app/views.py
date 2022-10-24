from django.shortcuts import render, redirect

from games_app.web_app.forms import CreateGameModelForm, EditeGameModelForm, DeleteGameModelForm, CreateProfileForm, \
    EditeProfileForm, DeleteProfileForm
from games_app.web_app.models import GameModel, Profile


def has_profile():
    profile = Profile.objects.first()
    if profile:
        return profile
    return None


# home
def show_index(request):
    if not Profile.objects.exists():
        redirect('create profile page')
    profile = has_profile()
    context = {
        'profile': profile
    }
    return render(request, 'home-page.html', context)


# dashboard
def show_dashboard(request):
    games = GameModel.objects.all()
    context = {
        'games': games
    }
    return render(request, 'dashboard.html', context)


# game
def create_game(request):
    if request.method == 'POST':
        form = CreateGameModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')
    else:
        form = CreateGameModelForm()
    context = {
        'form': form
    }

    return render(request, 'create-game.html', context)


def show_game(request, pk):
    game = GameModel.objects.get(pk=pk)
    context = {
        'game': game
    }

    return render(request, 'details-game.html', context)


def edite_game(request, pk):
    game = GameModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditeGameModelForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')
    else:
        form = EditeGameModelForm(instance=game)
    context = {
        'form': form
    }
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = GameModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteGameModelForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')
    else:
        form = DeleteGameModelForm(instance=game)
    context = {
        'form': form
    }
    return render(request, 'delete-game.html', context)


# profile
def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, )
        if form.is_valid():
            form.save()
            return redirect('dashboard page')
    else:
        form = CreateProfileForm()
    context = {
        'form': form
    }

    return render(request, 'create-profile.html', context)


def show_profile(request):
    games = GameModel.objects.all()
    game_count = 0
    game_rating = 0.0
    if GameModel.objects.exists():
        game_count = len(games)
        game_rating = sum([x.rating for x in games]) / game_count
    profile = has_profile()
    context = {
        'profile': profile,
        'game_count': game_count,
        'game_rating': game_rating,
    }
    return render(request, 'details-profile.html', context)


def edite_profile(request):
    profile = has_profile()

    if request.method == 'POST':
        form = EditeProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(' details profile page')
    else:
        form = EditeProfileForm(instance=profile)
    context = {
        'form': form
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
        'form': form
    }
    return render(request, 'delete-profile.html', context)
