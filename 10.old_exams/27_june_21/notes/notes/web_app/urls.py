from django.urls import path

from notes.web_app.views import show_index, add_note, edit_note, delete_note, show_details, show_profile, add_profile, \
    delete_profile

urlpatterns = (
    path('', show_index, name='home'),

    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', show_details, name='note details'),

    path('profile/', show_profile, name='profile'),
    path('profile/create/', add_profile, name='create profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
