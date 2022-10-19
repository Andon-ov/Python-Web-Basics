from django.template import Library

from music_app.web_app.models import Profile

register = Library()


@register.simple_tag()
def have_a_profile():
    profile = Profile.objects.all()
    try:
        return profile[0]
    except IndexError:
        return None
