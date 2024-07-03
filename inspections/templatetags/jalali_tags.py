# inspections/templatetags/jalali_tags.py

from django import template
import django_jalali

register = template.Library()

@register.filter(name='to_jalali')
def to_jalali(value, fmt='%y/%m/%d _ %H:%M:%S'):
    return django_jalali.datetime2jalali(value).strftime(fmt)
