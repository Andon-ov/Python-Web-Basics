from django.template import Library

from games_app.web_app.models import Profile

register = Library()


@register.simple_tag()
def have_a_profile():
    if Profile.objects.exists():
        return Profile.objects.first()
    return None
