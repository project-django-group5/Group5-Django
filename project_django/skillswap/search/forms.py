from django import forms
from skill.models import Skill

class SkillSearchForm(forms.Form):
    SKILL_TYPE_CHOICES = [
        ('', 'Choose any'),
        ('offer', 'Offer'),
        ('request', 'Request'),
    ]


    skill_type = forms.ChoiceField(
            required=False,
            choices=SKILL_TYPE_CHOICES,
            label='Skill Type'
        )
    category = forms.ChoiceField(required=False, label='Category')
    title = forms.ChoiceField(required=False, label='Title')
    location = forms.ChoiceField(required=False, label='Location')
    availability = forms.ChoiceField(required=False, label='Availability')

    def __init__(self, *args, **kwargs):
        dynamic_choices = kwargs.pop('dynamic_choices', {})
        super().__init__(*args, **kwargs)

        self.fields['category'].choices = [('', 'All')] + [ # type: ignore
            (cat, cat) for cat in dynamic_choices.get('categories', [])
        ]
        self.fields['title'].choices = [('', 'All')] + [ # type: ignore
            (title, title) for title in dynamic_choices.get('titles', [])
        ]
        self.fields['location'].choices = [('', 'All')] + [ # type: ignore
            (loc, loc) for loc in dynamic_choices.get('locations', [])
        ]
        self.fields['availability'].choices = [('', 'All')] + [ # type: ignore
            (avail, avail) for avail in dynamic_choices.get('availabilities', [])
        ]
