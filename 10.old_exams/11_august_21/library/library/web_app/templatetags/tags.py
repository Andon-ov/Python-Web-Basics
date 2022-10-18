from django.template import Library

from library.web_app.models import Profile

register = Library()


@register.simple_tag()
def have_a_profile():
    try:
        profile = Profile.objects.all()[0]
        return profile.first_name
    except IndexError:
        return None
