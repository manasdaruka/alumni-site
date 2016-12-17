from django import forms
from django.contrib.auth.models import User
from . import models


class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model =
        fields = ("first_name", "last_name", "email")
