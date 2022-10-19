from django.urls import path, include

from music_app.web_app.views import show_index, add_album, details_album, edit_album, delete_album, details_profile, \
    delete_profile, create_profile

urlpatterns = (
    path('', show_index, name='home page'),

    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', details_album, name='details album'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),
    path('profile/', include([
        path('details/', details_profile, name='profile details'),
        path('delete/', delete_profile, name='delete profile'),
        path('create/', create_profile, name='create profile'),
    ])),
)
