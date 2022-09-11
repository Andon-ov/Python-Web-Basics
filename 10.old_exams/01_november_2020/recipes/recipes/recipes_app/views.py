from django.shortcuts import render, redirect

from recipes.recipes_app.forms import EditRecipeForm, CreateRecipeForm, DeleteRecipeForm
from recipes.recipes_app.models import Recipe


def show_index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateRecipeForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditRecipeForm(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            # recipe.delete()
        return redirect('show index')

    else:
        form = DeleteRecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'delete.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')

    context = {

        'recipe': recipe,
        'ingredients': ingredients
    }

    return render(request, 'details.html', context)
