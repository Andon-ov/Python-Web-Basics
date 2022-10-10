from django.shortcuts import render, redirect

from cook_book.recipes.form import RecipeCreateForm
from cook_book.recipes.models import Recipe


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


def create_view(request):
    if request.method == 'POST':
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeCreateForm(request.POST)
        context = {
            'form': form
        }
        return render(request, 'create.html', context)

# class DetailsView(DetailView):
#     template_name = 'details.html'
#     queryset = Recipe.objects.get()
