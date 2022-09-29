from django.template import Library

from templates_demos.web.views import Student

register = Library()


# create simple tag
# Simple tag is a tag who always return string

@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return f'Hello, My name is {student.name} and I am {student.age}-years old'


# simple tag with many params
@register.simple_tag(name='simple_tag')
def simple_tag(*args, **kwargs):
    return ', '.join(str(x)
                     for
                     x in list(args) + list(kwargs.items()))


# inclusion tag
@register.inclusion_tag('tags/nav.html', name='app_nav', takes_context=False)
def generate_nav(*args):  # here can give and `context` - he come from `takes_context = True` (context,*args)
    return {
        'url_names': args,
    }
