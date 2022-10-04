from django.urls import path

from models_demos.web.views import index

urlpatterns = (
    path('', index, name='home'),
)
