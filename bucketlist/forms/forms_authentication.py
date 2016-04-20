"""Use django forms to generate registration and login forms."""
from django import forms
from django.core.exceptions import ObjectDoesNotExist

from bucketlist.models import Account


class RegistrationForm(forms.Form):
    """Create registration form with validation on fields.

    Check against existing users within models.
    """

    username = forms.RegexField(regex=r'^[0-9a-zA-Z_]*$',
                                max_length=30,
                                widget=forms.TextInput(attrs=dict(
                                    required=True,
                                    render_value=False)),
                                label='Username')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True,
                   render_value=False)),
        label='')
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True,
                   render_value=False)),
        label='')
    tagline = forms.CharField(widget=forms.TextInput(
        attrs=dict(required=True)),
        label='')

    def clean_username(self):
        """Check that the passed in username does not exist."""
        try:
            Account.objects.get(username=self.cleaned_data['username'])
        except ObjectDoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("This username has been used")

    def clean(self):
        """Check that the passed in password and confirmation match."""
        try:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError("Passwords do not match")
        except KeyError:
            return self.cleaned_data

    def save(self):
        """Save the newly created user."""
        new_user = Account.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        return new_user


class LoginForm(forms.Form):
    """Create login form with validation on fields."""

    username = forms.CharField(
        widget=forms.TextInput(attrs=dict({'autocomplete': 'off'})))
    password = forms.CharField(
        label='', max_length=100, widget=forms.PasswordInput)
