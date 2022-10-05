from django.template import Library

from music_app.my_music_app.models import Profile

register = Library()


@register.simple_tag()
def have_a_profile():
    return Profile.objects.count() > 0
