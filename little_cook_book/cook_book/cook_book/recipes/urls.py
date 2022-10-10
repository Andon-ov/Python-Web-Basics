from django.urls import path

from cook_book.recipes.views import index, details_view

urlpatterns = (
    path('', index, name='index'),
    # path('detail/<int:pk>/', DetailsView.as_view(), name='detail'),
    path('detail/<int:pk>/', details_view, name='detail'),
)
