from django.shortcuts import render


from cook_book.recipes.models import Recipe


def index(request):
    context = {
        'recipes': Recipe.objects.all(),

    }
    return render(request, 'index.html', context)


def details_view(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    context = {
        'ingredient': Recipe.objects.get(ingredient__unit_id=pk),
        'recipe': recipe,
    }
    return render(request, 'details.html', context)

# class DetailsView(DetailView):
#     template_name = 'details.html'
#     queryset = Recipe.objects.get()
