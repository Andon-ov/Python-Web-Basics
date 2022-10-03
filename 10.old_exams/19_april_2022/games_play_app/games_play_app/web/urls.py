from django.urls import path

from games_play_app.web.views import show_index, details_profile_page, edit_profile_page, \
    delete_profile_page, dashboard_page, details_game_page, create_game_page, edit_game_page, delete_game_page, \
    create_profile_page

urlpatterns = (
    path('', show_index, name='show index'),
    path('profile/create/', create_profile_page, name='create profile page'),  # func base view

    # path('profile/create/', CreateProfilePageView.as_view(), name='create profile page'), # clas base view

    path('profile/details/', details_profile_page, name='details profile page'),
    path('profile/edit/', edit_profile_page, name='edit profile page'),
    path('profile/delete/', delete_profile_page, name='delete profile page'),

    path('dashboard/', dashboard_page, name='dashboard page'),

    path('game/create/', create_game_page, name='create game page'),

    path('game/details/<int:pk>/', details_game_page, name='details game page'),
    path('game/edit/<int:pk>/', edit_game_page, name='edit game page'),
    path('game/delete/<int:pk>/', delete_game_page, name='delete game page'),

)

# urlpatterns = [
#     path('', views.show_index, name='home-page'),
#     path('dashboard/', views.dashboard_page, name='dashboard-page'),
#     path('profile/', include([
#         path('create/', views.create_profile_page, name='create-profile-page'),
#         path('details/', views.details_profile_page, name='profile-details-page'),
#         path('edit/', views.edit_profile_page, name='edit-profile-page'),
#         path('delete/', views.delete_profile_page, name='delete-profile-page'),
#     ])),
#     path('game/', include([
#         path('create/', views.create_game_page, name='create-game-page'),
#         path('details/<int:game_id>', views.details_game_page, name='game-details-page'),
#         path('edit/<int:game_id>', views.edit_game_page, name='edit-game-page'),
#         path('delete/<int:game_id>', views.delete_game_page, name='delete-game-page'),
#     ])),
# ]
