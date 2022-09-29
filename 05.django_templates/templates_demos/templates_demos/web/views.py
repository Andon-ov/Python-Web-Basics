import random
from datetime import datetime

from django.shortcuts import render, redirect


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
        'student_info': Student('Doncho', 19).get_info(),  # Right
        'now': datetime.now(),
        'students': ['Mariq', 'Pesho', 'Pesho', 'Pesho', 'Pesho', 'Gosho', 'Stamat'],
        'values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    }
    return render(request, 'index.html', context)


def redirect_to_home(request):
    return redirect('index')


def about(request):
    return render(request, 'about.html')
