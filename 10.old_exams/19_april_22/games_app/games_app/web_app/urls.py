from django.urls import path, include

from games_app.web_app.views import show_index, show_dashboard, create_game, show_game, edite_game, delete_game, \
    create_profile, show_profile, edite_profile, delete_profile

urlpatterns = (
    # home
    path('', show_index, name='home page'),
    # dashboard
    path('dashboard/', show_dashboard, name='dashboard page'),
    # game
    path('game/', include([
        path('create/', create_game, name='create game page'),
        path('details/<int:pk>/', show_game, name='details game page'),
        path('edit/<int:pk>/', edite_game, name='edit game page'),
        path('delete/<int:pk>/', delete_game, name='delete game page'),
    ])),
    # profile
    path('profile/', include([
        path('create/', create_profile, name='create profile page'),
        path('details/', show_profile, name=' details profile page'),
        path('edit/', edite_profile, name='edit profile page'),
        path('delete/', delete_profile, name='delete profile page'),
    ])),
)
