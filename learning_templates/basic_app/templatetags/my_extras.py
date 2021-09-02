from django import template

register = template.Library()

# Using decorator to register filter
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)