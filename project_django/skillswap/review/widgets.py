
from django.forms.widgets import RadioSelect
from django.utils.safestring import mark_safe

class StarRadioSelect(RadioSelect):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        final_attrs = self.build_attrs(attrs, name=name)
        for i in range(1, 6):
            checked = 'checked' if str(value) == str(i) else ''
            html = f'''
                <input type="radio" name="{name}" value="{i}" id="star{i}" {checked} hidden>
                <label for="star{i}">&#9733;</label>
            '''
            output.append(html)
        return mark_safe('<div class="star-rating">' + ''.join(output) + '</div>')
