from django.urls import path

from recipes.web_app.views import index, add_recipe, edit_recipe, delete_recipe, details_recipe

urlpatterns = (
    path('', index, name='home page'),
    path('create/', add_recipe, name='create recipe page'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe page'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe page'),
    path('details/<int:pk>/', details_recipe, name='recipe details page'),
)
