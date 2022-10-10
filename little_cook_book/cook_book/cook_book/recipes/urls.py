from django.urls import path

from cook_book.recipes.views import index, DetailsView

urlpatterns = (
    path('', index, name='index'),
    path('detail/<int:pk>/', DetailsView.as_view(), name='detail'),
)
