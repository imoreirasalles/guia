from django import template

register = template.Library()

@register.filter(name='subtract')
def subtract(value, arg):
     if arg and value != None:
         return value - arg
     else:
         return 0


@register.filter(name='add')
def add(value, arg):
     if arg and value != None:
         return value + arg
     else:
         return 0

@register.filter(name='percent')
def percent(value, arg):
     if arg and value != None and arg and value != 0 and arg < value:
         return 0
     else:
         return int((100*value)/(arg))
