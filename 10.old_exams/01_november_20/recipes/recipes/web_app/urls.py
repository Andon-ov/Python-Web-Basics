from django.urls import path

from recipes.web_app.views import index, create_recipe, edit_recipe, delete_recipe, show_recipe

urlpatterns = (
    path('', index, name='home page'),
    path('create/', create_recipe, name='create recipe page'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe page'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe page'),
    path('details/<int:pk>/', show_recipe, name='recipe details page'),
)
