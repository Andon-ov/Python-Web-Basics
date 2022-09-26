from django.urls import path

from petstagram.web.views.generics import show_index, show_dashboard
from petstagram.web.views.pets import create_pet_page, edit_pet_page, delete_pet_page
from petstagram.web.views.photos import like_photo_pet, add_photo_page, edit_photo_page, show_photo_details
from petstagram.web.views.profile import show_profile, create_profile_page, edit_profile_page, delete_profile_page

urlpatterns = [
    path('', show_index, name='show index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('profile/', show_profile, name='show profile'),
    path('profile/create/', create_profile_page, name='create profile page'),
    path('profile/edit/', edit_profile_page, name='profile edit page'),
    path('profile/delete/', delete_profile_page, name='profile delete page'),

    path('photo/details/<int:pk>/', show_photo_details, name='photo details'),
    path('photo/like/<int:pk>/', like_photo_pet, name='like pet photo'),
    path('photo/add/', add_photo_page, name='add photo page'),
    path('photo/edit/<int:pk>/', edit_photo_page, name='photo edit page'),

    path('pet/add/', create_pet_page, name='add pet page'),
    path('pet/edit/<int:pk>/', edit_pet_page, name='pet edit page'),
    path('pet/delete/<int:pk>/', delete_pet_page, name='pet delete page'),

]
