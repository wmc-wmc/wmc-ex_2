from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext


class SigninForm(forms.Form):
    username_or_email = forms.CharField(label="账号", max_length=255)
    password = forms.CharField(label="密码", max_length=100, widget = forms.PasswordInput)