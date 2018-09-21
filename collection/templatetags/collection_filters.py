from django import template

register = template.Library()

@register.filter(name='subtract')
def subtract(value, arg):
     if (value != None) & (arg != None) :
         if arg and value != None:
             return value - arg
         else:
             return 0
     else:
          return 0

@register.filter(name='percent')
def percent(value, arg):
      if (value != None) & (arg != None) :
          if (arg == 0) | (value == 0) | (int(arg) < int(value)) :
              return 0
          else:
              return int((100*value)/(arg))
      else:
          return 0

# Verbose name filter
@register.filter
def verbose_name_filter(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name
