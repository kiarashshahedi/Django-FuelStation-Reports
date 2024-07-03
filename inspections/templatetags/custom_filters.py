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