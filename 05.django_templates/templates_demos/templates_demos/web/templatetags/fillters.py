from django.template import Library

register = Library()

# build custom filters

@register.filter('odd')
def get_odd(value):
    return [x for x in value if x % 2 == 1]


@register.filter('app_style')
def format_to_app_style(data):
    return data.strftime('%y/%m/%d %H-%M-%S')
