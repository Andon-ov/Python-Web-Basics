from django.shortcuts import render, redirect
from django.views.generic import FormView

from cook_book.recipes.form import RecipeCreateForm, IngredientCreateForm
from cook_book.recipes.models import Recipe, Ingredient


def index(request):
    context = {
        'recipes': Recipe.objects.all(),

    }
    return render(request, 'index.html', context)


def details_view(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    context = {
        'recipe': recipe,
    }
    return render(request, 'details.html', context)


def create_recipe_view(request):
    if request.method == 'POST':
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeCreateForm()
        context = {
            'form': form
        }
        return render(request, 'create-recipe.html', context)


# def create_ingredient_view(request):
#     if request.method == 'POST':
#         form = IngredientCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = IngredientCreateForm()
#         context = {
#             'form': form
#         }
#         return render(request, 'create-ingredient.html', context)


class CreateIngredientView(FormView):
    template_name = 'create-ingredient.html'
    form_class = IngredientCreateForm
    success_url = '/create/ingredient/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
