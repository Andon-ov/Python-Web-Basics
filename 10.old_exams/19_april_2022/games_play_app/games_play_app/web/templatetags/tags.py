from django.template import Library

from games_play_app.web.models import ProfileModel

register = Library()


@register.simple_tag()
def have_a_profile():  # here can give and `context` - he come from `takes_context = True` (context,*args)
    return ProfileModel.objects.count() > 0
