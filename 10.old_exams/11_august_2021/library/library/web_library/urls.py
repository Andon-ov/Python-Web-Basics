from django.urls import path

from library.web_library.views import home_page, add_book_page, edit_book_page, book_details_page, profile_page, \
    edit_profile_page, delete_profile_page, create_profile_page, delete_book_page

urlpatterns = [
    path('', home_page, name='show index'),
    path('add/', add_book_page, name='add book page'),
    path('edit/<int:pk>', edit_book_page, name='edit book page'),
    path('delete/<int:pk>', delete_book_page, name='delete book page'),
    path('details/<int:pk>', book_details_page, name='book details page'),

    path('profile/', profile_page, name='profile page'),
    path('create/', create_profile_page, name='create profile page'),
    path('profile/edit/', edit_profile_page, name='edit profile page'),
    path('profile/delete/', delete_profile_page, name='delete profile page'),
]
