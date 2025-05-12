from django import template

register = template.Library()

@register.filter
def is_seller(user):
    """Check if the user is a seller"""
    return hasattr(user, 'selleruser')
