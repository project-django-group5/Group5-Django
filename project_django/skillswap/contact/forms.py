from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'message', 'sender', 'receiver', 'subject', 'sent_time']
        
        