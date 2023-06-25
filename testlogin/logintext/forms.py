from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Profile


class ProfileForm(UserCreationForm):
    nickname = forms.CharField(max_length=30)

    class Meta:
        model = Profile
        fields = ['username', 'nickname']

