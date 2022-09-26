from django.shortcuts import render


# Create your views here.
def simple_view(request):
    context = {
        'view': 'This is my view - I`M the best!!!',
    }

    return render(request, 'simlpe.html', context)
