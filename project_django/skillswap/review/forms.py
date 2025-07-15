from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
<<<<<<< HEAD
            'rating': forms.RadioSelect(choices=[(i, '') for i in range(1, 5)]),
=======
            'rating': forms.RadioSelect(choices=[(i, '') for i in range(1, 6)]),
>>>>>>> 9e8f17c89ae934e7c13571a9db77a0d7a0d9fb2e
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review...'})
        }

