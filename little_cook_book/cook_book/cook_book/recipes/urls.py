from django.urls import path

from cook_book.recipes.views import index

urlpatterns = (
    path('', index, name='index'),
)
