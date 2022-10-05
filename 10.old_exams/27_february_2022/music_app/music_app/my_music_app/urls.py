from django.urls import path, include

from music_app.my_music_app.views import add_album, details_album, edit_album, delete_album, \
    profile_details, profile_delete, profile_create, show_index

urlpatterns = (

    path('', show_index, name='index'),


    path('album/', include([

        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', details_album, name='details album'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ]), ),

    path('profile/', include([
        path('details/', profile_details, name='profile details'),
        path('create/', profile_create, name='profile create'),
        path('delete/', profile_delete, name='profile delete'),
    ]), ),

)
