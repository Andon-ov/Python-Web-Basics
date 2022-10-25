from django.shortcuts import render, redirect

from recipes.web_app.forms import RecipeCreateForm, RecipeEditeForm, RecipeDeleteForm
from recipes.web_app.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = RecipeCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = RecipeEditeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = RecipeEditeForm(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = RecipeDeleteForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = RecipeDeleteForm(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'delete.html', context)


def show_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    all_ingredients = [x for x in recipe.ingredients.split(', ')]

    context = {
        'all_ingredients': all_ingredients,
        'recipe': recipe,
    }
    return render(request, 'details.html', context)
