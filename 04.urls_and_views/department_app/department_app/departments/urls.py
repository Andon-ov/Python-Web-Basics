from django.urls import path

from department_app.departments.views import simple_view

urlpatterns = [
    path('', simple_view, name='simple view')
]
