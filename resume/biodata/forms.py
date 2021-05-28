from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ResumeUser
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

COUNTRY_CHOICE = (
    ('india', 'india'),
    ('japan', 'japan'),
    ('china', 'china'),
)
GENDER_CHOICE = (
    ('male', 'male'),
    ('female', 'female'),
)


def isempty_first(value):
    if value == ' ':
        raise forms.ValidationError("This is can not empty")


def isempty_last(value):
    if value == ' ':
        raise forms.ValidationError("This is can not empty")


def isempty_email(value):
    if value == ' ':
        raise forms.ValidationError("This is can not empty")
    # elif User.objects.filter(email=value).exists():
    #     raise forms.ValidationError("Email is already exists")


def isreset_email(value):
    if value == ' ':
        raise forms.ValidationError("This is can not empty")
    elif not User.objects.filter(email=value).exists():
        raise forms.ValidationError("Email is not exists.")


def isexist_user(value):
    if not User.objects.filter(username=value).exists():
        raise forms.ValidationError("usesr is not exists")


class ResumeForm(UserCreationForm):
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your confirm password :', 'class': 'form-control'}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your  password :', 'class': 'form-control'}))
    first_name = forms.CharField(validators=[isempty_first], widget=forms.TextInput(
        attrs={'placeholder': 'Enter  First name :', 'class': 'form-control'}),)
    last_name = forms.CharField(validators=[isempty_last], widget=forms.TextInput(
        attrs={'placeholder': 'Enter  last name :', 'class': 'form-control'}),)
    email = forms.EmailField(validators=[isempty_email], widget=forms.EmailInput(
        attrs={'placeholder': 'Enter your email :', 'class': 'form-control'}),)

    country = forms.ChoiceField(choices=COUNTRY_CHOICE, widget=forms.Select(attrs={
                                'class': 'form-control'}),)
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.Select(attrs={
        'class': 'form-control'}),)

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


class LoginForm(AuthenticationForm):
    username = forms.CharField(validators=[isexist_user],
                               label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter your  username :', 'class': 'form-control'}))
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your  password :', 'class': 'form-control'}))


class ResetForm(PasswordResetForm):
    email = forms.EmailField(validators=[isreset_email], widget=forms.EmailInput(
        attrs={'placeholder': 'Enter your email :', 'class': 'form-control'}),)


class ResetConfirmForm(SetPasswordForm):
    new_password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your confirm password :', 'class': 'form-control'}))
    new_password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your  password :', 'class': 'form-control'}))
