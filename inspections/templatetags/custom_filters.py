# inspections/templatetags/extras.py

from django import template

register = template.Library()

@register.filter
def times(number):
    return range(number)

@register.filter
def subtract(value, arg):
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return None
    
    

@register.filter
def strip_zero(value):
    try:
        # Check if the value is a float and convert it to string
        value = str(float(value))
        # Check if the string representation ends with '.0' and strip it
        if value.endswith('.0'):
            return value[:-2]
        return value
    except (ValueError, TypeError):
        return value