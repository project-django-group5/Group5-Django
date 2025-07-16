from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter("star_rating")
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

    html = '<i class="fas fa-star text-warning"></i>' * full
    if half:
        html += '<i class="fas fa-star-half-alt text-warning"></i>'
    html += '<i class="far fa-star text-warning"></i>' * empty

    return mark_safe(html)

