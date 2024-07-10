from django import template
from khayyam import JalaliDate




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
    
    
    
@register.filter
def to_gregorian(persian_date):
    if not persian_date:
        return ''
    try:
        j_date = JalaliDate(persian_date)
        g_date = j_date.todate()
        return g_date.strftime('%Y-%m-%d')
    except Exception as e:
        return ''