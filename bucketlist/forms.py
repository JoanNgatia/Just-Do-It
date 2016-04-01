import re
from django import forms
from django.core.exceptions import ObjectDoesNotExist

from models import Account
# from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^[0-9a-zA-Z_]*$', max_length=30,
                                widget=forms.TextInput(attrs=dict(
                                    required=True,
                                    render_value=False)),
                                label='username')
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(
        required=True, render_value=False)), label='password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, render_value=False)),
        label='Confirm password')
    tagline = forms.CharField(widget=forms.TextInput,
                              label='Favorite Catchphrase')

    def clean_username(self):
        try:
            Account.objects.get(username=self.cleaned_data['username'])
        except ObjectDoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("This username has been used")

    def clean(self):
        try:
            if self.cleaned_data['password'] != self.cleaned_data['verify_password']:
                raise forms.ValidationError("Passwords do not match")
        except KeyError:
            return self.cleaned_data

    def save(self):
        new_user = Account.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        return new_user


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=dict({
        'placeholder': 'Enter unique username',
        'autocomplete': 'off'
    })))
    password = forms.CharField(
        label='Password', max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '**********'
            }))
