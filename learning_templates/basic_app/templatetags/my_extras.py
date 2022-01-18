from django import template


register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all the values of "arg" from the string!
    """

    return value.replace(arg, '')

# We are going to use decorator for the same,
# register.filter('cut', cut)
