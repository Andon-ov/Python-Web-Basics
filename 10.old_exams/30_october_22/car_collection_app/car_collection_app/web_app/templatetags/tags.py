from django.template import Library

from car_collection_app.web_app.models import Profile

register = Library()


@register.simple_tag()
def have_a_profile():
    if Profile.objects.exists():
        profile = Profile.objects.first()
        return profile.username
    return None
