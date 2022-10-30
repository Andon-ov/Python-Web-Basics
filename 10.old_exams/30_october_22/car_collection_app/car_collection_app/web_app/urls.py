from django.urls import path, include

from car_collection_app.web_app.views import show_index, show_catalogue, create_car, show_car, edit_car, delete_car, \
    create_profile, show_profile, edit_profile, delete_profile

urlpatterns = (
    # index
    path('', show_index, name='index'),
    # catalogue
    path('catalogue/', show_catalogue, name='catalogue'),
    # create car
    path('car/create/', create_car, name='create car'),
    # create
    path('car/<int:pk>/', include([
        path('details/', show_car, name='show car'),
        path('edit/', edit_car, name='edit car'),
        path('delete/', delete_car, name='delete car'),

    ]), ),
    # create profile
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', show_profile, name='show profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
