from django.urls import path, include

from cook_book.recipes.views import index, details_view, create_recipe_view, CreateIngredientView

urlpatterns = (
    path('', index, name='index'),
    # path('detail/<int:pk>/', DetailsView.as_view(), name='detail'),
    path('detail/<int:pk>/', details_view, name='detail'),

    path('create/', include(
        [path('recipe/', create_recipe_view, name='create recipe'),
         # path('ingredient/', create_ingredient_view, name='create ingredient'),
         path('ingredient/', CreateIngredientView.as_view(), name='create ingredient'),
     ])))
