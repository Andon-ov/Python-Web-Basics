from django.urls import path, include

from library.web_app.views import show_index, add_book, edit_book, show_book_details, show_profile, edit_profile, \
    delete_profile, add_profile, delete_book

urlpatterns = (
    path('', show_index, name='home page'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('details/<int:pk>/', show_book_details, name='book details'),
    path('profile/', include([
        path('', show_profile, name='profile'),
        path('add/', add_profile, name='add profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))

)
