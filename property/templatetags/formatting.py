from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def intdot(value):
    try:
        return intcomma(int(float(value))).replace(",", ".")
    except (ValueError, TypeError):
        return value
