from django import forms
from .models import Review
from .widgets import StarRadioSelect

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': StarRadioSelect(),
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review...'})
        }
