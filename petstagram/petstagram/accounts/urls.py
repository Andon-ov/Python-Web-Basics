from django.urls import path, include

from petstagram.accounts.views import delete_user, register_user, login_user, edit_user, details_user

urlpatterns = [
    path('login/', login_user, name='login user'),
    path('register/', register_user, name='register user'),
    path('profile/<int:pk>/', include([

        path('delete/', delete_user, name='delete user'),
        path('edit/', edit_user, name='edit user'),
        path('', details_user, name='details user'),

    ])),
]
