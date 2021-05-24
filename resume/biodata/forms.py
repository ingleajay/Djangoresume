from .models import ResumeUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core import validators


def isempty_first(value):
    if value == ' ':
        raise forms.ValidationError("This is can not empty")


def isempty_last(value):
    if value == ' ':
        raise forms.ValidationError("This is can not empty")


def isempty_email(value):
    if value == ' ':
        raise forms.ValidationError("This is can not empty")


class ResumeForm(UserCreationForm):
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your confirm password :', 'class': 'form-control'}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your  password :', 'class': 'form-control'}))
    first_name = forms.CharField(validators=[isempty_first], widget=forms.TextInput(
        attrs={'placeholder': 'Enter  First name :', 'class': 'form-control'}),)
    last_name = forms.CharField(validators=[isempty_last], widget=forms.TextInput(
        attrs={'placeholder': 'Enter  last name :', 'class': 'form-control'}),)
    email = forms.EmailField(validators=[isempty_email], widget=forms.TextInput(
        attrs={'placeholder': 'Enter your email :', 'class': 'form-control'}),)

    class Meta:
        model = ResumeUser

        fields = ['username', 'first_name', 'last_name',
                  'email', 'city', 'country', 'gender', 'profile_image']
        labels = {'username': 'Enter Username ', 'first_name': 'Enter Your first  name',
                  'last_name': 'Enter Your last name', 'email': 'Enter Your Email', }
        widgets = {'username': forms.TextInput(
            attrs={'placeholder': 'Enter your username:', 'class': 'form-control'}),
            'city': forms.TextInput(
            attrs={'placeholder': 'Enter your city :', 'class': 'form-control'}),
            'profile_image': forms.FileInput(
            attrs={'placeholder': 'choose your profile image :', 'class': 'form-control'}),
        }
