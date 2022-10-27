from django.template import Library

from library.web_app.models import Profile

register = Library()


@register.simple_tag()
def have_a_profile():
    if Profile.objects.exists():
        profile = Profile.objects.first()
        return profile.first_name
    return None
