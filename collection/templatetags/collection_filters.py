from django import template

register = template.Library()

@register.filter(name='subtract')
def subtract(value, arg):
    return value - arg

@register.filter(name='add')
def add(value, arg):
    return value + arg

@register.filter(name='percent')
def percent(value, arg):
    if arg< value:
        return 0
    else:
        return int((100*value)/(arg))
