from django import template

register = template.Library()

@register.filter
def star_rating(value):
    try:
        value = round(float(value))
    except (TypeError, ValueError):
        value = 0

    full_stars = int(value)
    empty_stars = 5 - full_stars

    return '★' * full_stars + '☆' * empty_stars
