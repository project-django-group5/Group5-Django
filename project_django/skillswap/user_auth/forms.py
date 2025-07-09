from django import forms
from django.contrib.auth.models import User
from .models import UserDetail

# Both UserForm and RegistrationForm are used to signup/register the user


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class RegistrationForm(forms.ModelForm):
    class Meta():
        model = UserDetail
        fields = ('description', 'skills_offered',
                  'skills_needed', 'profile_pic')


# LoginForm used to login the user
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'password')


# from django.contrib.auth.forms import AuthenticationForm
# # Used to log in existing users (uses built-in auth form)
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))