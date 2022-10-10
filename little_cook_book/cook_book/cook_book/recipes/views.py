from django.shortcuts import render
from django.views.generic import DetailView

from cook_book.recipes.models import Recipe


def index(request):
    context = {
        'recipes': Recipe.objects.all(),

    }
    return render(request, 'index.html', context)


class DetailsView(DetailView):
    template_name = 'details.html'
    queryset = Recipe.objects.get()
