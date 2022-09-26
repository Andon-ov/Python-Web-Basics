from django import template

from petstagram.web.models import Profile

register = template.Library()


@register.simple_tag()
def hes_profile():
    return Profile.objects.count() > 0


