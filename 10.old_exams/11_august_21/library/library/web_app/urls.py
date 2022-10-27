from django.urls import path, include

from library.web_app.views import show_index, add_book, edit_book, show_book, show_profile, edite_profile, \
    delete_profile, delete_book, create_profile

urlpatterns = (
    path('', show_index, name='home'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('details/<int:pk>/', show_book, name='show book'),

    path('profile/', include([
        path('', show_profile, name='show profile'),
        path('create/', create_profile, name='create profile'),
        path('edit/', edite_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),

)
