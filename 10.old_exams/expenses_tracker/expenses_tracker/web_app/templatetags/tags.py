from django.template import Library

from expenses_tracker.web_app.models import Profile

register = Library()


@register.simple_tag()
def have_a_profile():
    return Profile.objects.count() > 0
