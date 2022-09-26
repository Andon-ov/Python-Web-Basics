from django.urls import path

from templates_demos.web.views import show_index

urlpatterns = [
    path('', show_index, name='index')
]
