from django.template import Library

from notes.web_notes.models import Profile

register = Library()


@register.simple_tag()
def have_a_profile():
    return Profile.objects.count() > 0
