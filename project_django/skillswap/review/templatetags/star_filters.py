from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def star_rating(value):
    try:
        value = float(value)
    except (TypeError, ValueError):
        return '☆☆☆☆☆'

    full = int(value)
    half = 1 if value - full >= 0.25 and value - full < 0.75 else 0
    if value - full >= 0.75:
        full += 1
        half = 0
    empty = 5 - full - half

    html = '<span class="star full">★</span>' * full
    if half:
        html += '<span class="star half">★</span>'
    html += '<span class="star empty">★</span>' * empty

    return mark_safe(html)
