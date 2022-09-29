from django.urls import path, include

urlpatterns = (
    path('add/', add_photo, name='photo add'),
    path('<int:pk>/', include([
        path('', details_photo, name='photo details'),
        path('edit/ ', edit_photo, name='photo edit'),
    ])),
)
