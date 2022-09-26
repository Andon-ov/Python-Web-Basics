import random
from datetime import datetime

from django.shortcuts import render


class Student:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_info(self):
        return f'Name: {self.name}; Age: {self.age}'


# Create your views here.


def show_index(request):
    context = {
        'title': 'SoftUni Homepage',
        'value': random.random(),
        'info': {
            'address': 'Sofia'
        },
        'student': Student('Doncho', 19),  # Wrong
        'student_info': Student('Doncho', 19).get_info(),# Right
        'now': datetime.now()
    }
    return render(request, 'index.html', context)
